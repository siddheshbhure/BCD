from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render,redirect, render_to_response, get_object_or_404
# from .forms import TFAForm
from django.db import models
from .models import BCD,COEHead,FinanceHead,CIOHead,PR,GovHead
from datetime import datetime, timedelta
import requests
import xml.etree.ElementTree as ET
from django.http import HttpResponse, JsonResponse, Http404
from datetime import datetime, timedelta
import os
from django.conf import settings
from .forms import BCDModelForm,BCDModelCOEForm,BCDModelFINForm,BCDModelCIOForm,PRModelForm,PRMemberFormSet,PRMemberFormSetView,BCDModelFinalForm
from django.template import RequestContext
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.db import transaction
from .decorators import custom_login_required

# Create your views here.

def LoginView(request):
	if request.method=='POST':
		uname=request.POST['username']
		COE=COEHead.objects.filter(COE_ID=uname)
		FIN=FinanceHead.objects.filter(Fin_ID=uname)
		CIO=CIOHead.objects.filter(CIO_ID=uname)
		GOV=GovHead.objects.filter(Gov_ID=uname)
		if COE:
			if request.POST['password']=='Welcome123':
				print('in COE..')
				request.session['username']=uname
				return redirect('bcd-list-COE')
			else:
				return render(request,'login-new.html',{'msg':'Invalid Credentials Please try again.!'})
		elif FIN:
			if request.POST['password']=='Welcome123':
				print('in FIN..')
				request.session['username']=uname
				return redirect('bcd-list-FIN')
			else:
				return render(request,'login-new.html',{'msg':'Invalid Credentials Please try again.!'})
		elif CIO:
			if request.POST['password']=='Welcome123':
				print('in CIO..')
				request.session['username']=uname
				return redirect('bcd-list-CIO')
			else:
				return render(request,'login-new.html',{'msg':'Invalid Credentials Please try again.!'})
		elif GOV:
			if request.POST['password']=='Welcome123':
				print('in GOV..')
				request.session['username']=uname
				return redirect('bcd-list-Final')
			else:
				return render(request,'login-new.html',{'msg':'Invalid Credentials Please try again.!'})
		else:
			if request.POST['username']=='BCDUser' and request.POST['password']=='Welcome123':
				request.session['username']=uname
				return redirect('bcd-list')
			else:

				return render(request,'login-new.html',{'msg':'Invalid Credentials Please try again.!'})	

	return render(request, 'login-new.html')

def LogoutView(request):
	request.session.flush()
	return render(request,'login-new.html')

def logoutpage(request):
	return render(request,'logoutpage.html')

@custom_login_required
def bcdListView(request):
	bcd_list = BCD.objects.all()
	username=request.session.get('username')
	return render(request,'bcd-list.html',{'bcd_list':bcd_list,'username':username})

@custom_login_required
def bcdListCOEView(request):
	bcd_list_COE=BCD.objects.filter(FirstApproval__COE_Name='Abhimanyu Bhateja',status='Pending with COE Head.')
	username=request.session.get('username')
	return render(request,'bcd-list-COE.html',{'bcd_list_COE':bcd_list_COE,'username':username})

@custom_login_required
def bcdListFINView(request):
	bcd_list_FIN=BCD.objects.filter(status='Pending with Tech Finance.')
	username=request.session.get('username')
	return render(request,'bcd-list-FIN.html',{'bcd_list_FIN':bcd_list_FIN,'username':username})

@custom_login_required
def bcdListCIOView(request):
	bcd_list_CIO=BCD.objects.filter(status='Pending with CIO.')
	username=request.session.get('username')
	return render(request,'bcd-list-CIO.html',{'bcd_list_CIO':bcd_list_CIO,'username':username})

@custom_login_required
def bcdListFinalView(request):
	bcd_list_Final=BCD.objects.filter(status='Pending with Governance Head.')
	print("in final"+str(bcd_list_Final))
	username=request.session.get('username')
	return render(request,'bcd-list-Final.html',{'bcd_list_Final':bcd_list_Final,'username':username})

@custom_login_required
def DashboardView(request):
    return render(request, 'dashboard.html')


class CreateNewBCD(CreateView):
	form_class=BCDModelForm
	model=BCD
	template_name='BCD_form.html'
	
	def form_valid(self,form):
		d = datetime.now()
		bcd_list = BCD.objects.all()
		temp_no='BCD'+d.strftime("%d%m%y")
		exists = BCD.objects.filter(BCD_no__icontains=temp_no)
		if not exists:
			bcdnumber='BCD'+d.strftime("%d%m%y")+'01'
		else:
			for e in exists:
				count = e.BCD_no[-2:]
			finalcount = int(count) + 1;
			finalcount = str(finalcount).zfill(2)
			bcdnumber = ('BCD'+d.strftime("%d%m%y")+finalcount)

		self.object = form.save()
		self.object.requestor_ID='BCDUser'
		self.object.requestor_name='BCDUser'
		self.object.BCD_no=bcdnumber
		self.object.status='Pending with COE Head.'
		self.object.save()
		return render(self.request,'bcd-list.html',{'bcd_list':bcd_list,'msg':'request sent successfully..'})



class UpdateBCD(UpdateView):
	form_class=BCDModelForm
	model=BCD
	template_name='edit-form.html'

	# fields=['BCD_no','BCD_amount','BCD_overview','FirstApproval','pdf']
	def get_context_data(self,**kwargs):
		context = super(UpdateBCD, self).get_context_data(**kwargs)
		context['BCD_no'] = self.object.BCD_no
		return context

		#return HttpResponse(render(request,'edit-form.html',context))

	def form_valid(self,form):
		self.object=form.save()
		self.object.status='Pending with COE Head.'
		bcd_list = BCD.objects.all()
		return render(self.request,'bcd-list.html',{'bcd_list':bcd_list,'msg':'Data saved successfully..'})


class UpdateBCDCOE(UpdateView):
	form_class=BCDModelCOEForm
	model=BCD
	template_name='edit-form-COE.html'

	def get_context_data(self,**kwargs):
		context = super(UpdateBCDCOE, self).get_context_data(**kwargs)
		context['BCD_no'] = self.object.BCD_no
		context['pdf']= self.object.pdf
		return context

	def form_valid(self,form):
		print(self.request.POST)
		if 'Approve' in  self.request.POST:
			self.object=form.save()
			self.object.status='Pending with CIO.'
			self.object.COE_status='Approved'
			self.object.save()
			bcd_list_COE=BCD.objects.filter(FirstApproval__COE_Name='Abhimanyu Bhateja',status='Pending with COE Head.')
			return render(self.request,'bcd-list-COE.html',{'bcd_list_COE':bcd_list_COE,'msg':'Data saved successfully..'})
		else:			
			self.object=form.save()
			self.object.status='Rejected By COE Head'
			self.object.COE_status='Rejected'
			self.object.save()
			bcd_list_COE=BCD.objects.filter(FirstApproval__COE_Name='Abhimanyu Bhateja',status='Pending with COE Head.')
			return render(self.request,'bcd-list-COE.html',{'bcd_list_COE':bcd_list_COE,'msg':'Data saved successfully..'})

	def form_invalid(self,form):
		return HttpResponse(form.errors)



class UpdateBCDFIN(UpdateView):
	form_class=BCDModelFINForm
	model=BCD
	template_name='edit-form-FIN.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['username']=self.request.session.get('username')
		context['BCD_no'] = self.object.BCD_no
		context['pdf']= self.object.pdf
		return context

	def form_valid(self,form):
		if 'Approve' in self.request.POST:
			print('IN approve Fin.')
			self.object=form.save()
			self.object.status='Pending with CIO.'
			self.object.Finance_status='Approved'
			self.object.save()
			bcd_list_FIN=BCD.objects.filter(status='Pending with Tech Finance.')
			return render(self.request,'bcd-list-FIN.html',{'bcd_list_FIN':bcd_list_FIN,'msg':'Data saved successfully..'})
		else:
			print('out reject Fin.')
			self.object=form.save()
			self.object.status='Rejected By Finance'
			self.object.Finance_status='Rejected'
			self.object.save()
			bcd_list_FIN=BCD.objects.filter(status='Pending with Tech Finance.')
			return render(self.request,'bcd-list-FIN.html',{'bcd_list_FIN':bcd_list_FIN,'msg':'Data saved successfully..'})


class UpdateBCDCIO(UpdateView):
	form_class=BCDModelCIOForm
	model=BCD
	template_name='edit-form-CIO.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['username']=self.request.session.get('username')
		context['BCD_no'] = self.object.BCD_no
		context['pdf']= self.object.pdf
		return context

	def form_valid(self,form):
		if 'Approve' in self.request.POST:
			self.object=form.save()
			self.object.CIO_status='Approved'
			if int(self.object.BCD_amount) >=5000000:
				self.object.status='Pending with Governance Head.'
			else:
				self.object.status='Approved'
			self.object.save()
			bcd_list_CIO=BCD.objects.filter(status='Pending with CIO.')
			return render(self.request,'bcd-list-CIO.html',{'bcd_list_CIO':bcd_list_CIO,'msg':'Data saved successfully..'})
		else:
			self.object=form.save()
			self.object.status='Rejected By CIO'
			self.object.CIO_status='Rejected'
			self.object.save()
			bcd_list_CIO=BCD.objects.filter(status='Pending with CIO.')
			return render(self.request,'bcd-list-CIO.html',{'bcd_list_CIO':bcd_list_CIO,'msg':'Data saved successfully..'})



class UpdateBCDFinal(UpdateView):
	form_class=BCDModelFinalForm
	model=BCD
	template_name='edit-form-Final.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['username']=self.request.session.get('username')
		context['BCD_no'] = self.object.BCD_no
		context['pdf']= self.object.pdf
		return context

	def form_valid(self,form):
		if 'Approve' in self.request.POST:
			self.object=form.save()
			self.object.status='Approved'
			self.object.Final_status='Approved'
			self.object.save()
			bcd_list_Final=BCD.objects.filter(status='Pending with Governance Head.')
			return render(self.request,'bcd-list-Final.html',{'bcd_list_Final':bcd_list_Final,'msg':'Data saved successfully..'})
		else:
			self.object=form.save()
			self.object.status='Rejected By Governance Head'
			self.object.Final_status='Rejected'
			self.object.save()
			bcd_list_Final=BCD.objects.filter(status='Pending with Governance Head.')
			return render(self.request,'bcd-list-Final.html',{'bcd_list_Final':bcd_list_Final,'msg':'Data saved successfully..'})



class CreateNewBCDCOE(CreateView):
	form_class=BCDModelForm
	model=BCD
	template_name='BCD_form_COE.html'
	
	def form_valid(self,form):
		d = datetime.now()
		bcd_list_COE=BCD.objects.filter(FirstApproval__COE_Name='Abhimanyu Bhateja')
		temp_no='BCD'+d.strftime("%d%m%y")
		exists = BCD.objects.filter(BCD_no__icontains=temp_no)
		if not exists:
			bcdnumber='BCD'+d.strftime("%d%m%y")+'01'
		else:
			for e in exists:
				count = e.BCD_no[-2:]
			finalcount = int(count) + 1;
			finalcount = str(finalcount).zfill(2)
			bcdnumber = ('BCD'+d.strftime("%d%m%y")+finalcount)

		self.object = form.save()
		self.object.requestor_ID='08866'
		self.object.requestor_name='08866'
		self.object.BCD_no=bcdnumber
		self.object.status='Pending with COE'
		self.object.save()
		return render(self.request,'bcd-list-COE.html',{'bcd_list_COE':bcd_list_COE,'msg':'request sent successfully..'})

# def PRView(request):
# 	username=request.session.get('username')
# 	return render(request,'PR_form.html')

class PRMember(CreateView):
	model=PR

class PRMemberCreate(CreateView):
	model=PR
	form_class=PRModelForm
	# fields=['Application_system','Budget','Business','start_date','end_date','Number_of_months']
	template_name = 'pr_form.html'
	# success_url = 

	def get_context_data(self,**kwargs):
		bcdobj=BCD.objects.get(BCD_no=self.kwargs['string'])
		data=super(PRMemberCreate, self).get_context_data(**kwargs)
		if self.request.POST:
			# print('yeee...'+str(self.request.POST))
			data['PRmembers'] = PRMemberFormSet(self.request.POST)
			bcdobj.isPRRaised=True
			bcdobj.save()
			# data['menu']='newloan'
		else:
			b=BCD.objects.get(BCD_no=self.kwargs['string'])
			data['PRmembers'] = PRMemberFormSet()
			# data['menu']='newloan'
			data['BCD_no']=self.kwargs['string']
			data['BCD_amount']=b.BCD_amount
			data['PRs']=bcdobj.PRs.all()
			data['username']=self.request.session['username']
			data['firstapproval']=b.FirstApproval
			
			print(self.request)
		return data

	def form_valid(self,form):
		d = datetime.now()
		context = self.get_context_data()
		PRmembers = context['PRmembers']


		exists = PR.objects.filter(PR_No__icontains=self.kwargs['string']+'PR').order_by('id')
		if not exists:
			temp_pr=self.kwargs['string']+'PR01'
		else:
			for e in exists:
				count = e.PR_No[-2:]
			finalcount = int(count) + 1
			finalcount = str(finalcount).zfill(2)
			temp_pr = (self.kwargs['string'] +'PR'+ finalcount)
		
		self.object = form.save()
		self.object.PR_No=temp_pr
		# print('yeee raised..')
		self.object.isPRRaised=True
		self.object.Request_date=d.strftime("%d%m%y")
		self.object.BCD_no_id=id=BCD.objects.get(BCD_no=self.kwargs['string']).id
		self.object.save()

		if PRmembers.is_valid():
			PRmembers.instance = self.object
			PRmembers.save()
			self.kwargs['msg']='data saved successfully'
			return redirect('view-pr',self.kwargs['string'],self.object.pk,1)
		else:
			# print('oyee..!')
			return redirect('view-pr',self.kwargs['string'],self.object.pk,1)
		return redirect('view-pr',self.kwargs['string'],self.object.pk,1)

	def form_invalid(self,form):
		return HttpResponse(form.errors)


class PRMemberUpdate(UpdateView):
	model=PR
	form_class=PRModelForm
	# fields=['Application_system','Budget','Business','start_date','end_date','Number_of_months']
	template_name = 'PR_update.html'

	def get_context_data(self,**kwargs):
		data=super(PRMemberUpdate, self).get_context_data(**kwargs)
		if self.request.POST:  # executes when a new loan is created, after def form_valid (below function)
			data['PRmembers'] = PRMemberFormSet(self.request.POST, self.request.FILES,instance=self.object)
			data['menu']='newloan'
		else:
			bcdobj=BCD.objects.get(BCD_no=self.kwargs['string'])
			p=PR.objects.get(PR_No=self.object.PR_No)
			if p.Grids.all():             # If there is no document in the application, then atleast one row to add document should be visible in update loan form
				data['PRmembers'] = PRMemberFormSetView(instance=self.object)
			else:							# If there are documents, then new row for adding a new document should NOT be visible. new row can e added by clicking Add Document
				data['PRmembers'] = PRMemberFormSet(instance=self.object)
			# data['PRmembers'] = PRMemberFormSet()
			data['menu']='newloan'
			data['BCD_no']=self.kwargs['string']
			data['PR_No']=self.object.PR_No
			data['BCD_amount']=BCD.objects.get(BCD_no=self.kwargs['string']).BCD_amount
			data['prpk']=self.kwargs['pk']
			data['PRs']=bcdobj.PRs.all()
			data['username']=self.request.session['username']
			if self.kwargs['fl'] == '1':
				print('yee..'+self.kwargs['fl'])
				data['msg']='PR Created successfully..!'
			else:
				pass
			# if self.object.Budget:
			# 	data['msg']='successfully'
		return data

	def form_valid(self,form):
		d = datetime.now()
		context = self.get_context_data()
		PRmembers = context['PRmembers']
		self.object = form.save()
		self.object.PR_No=self.kwargs['string']+'PR01'
		self.object.Request_date=d.strftime("%d%m%y")
		self.object.save()

		if PRmembers.is_valid():
			PRmembers.instance = self.object
			PRmembers.save()
		return redirect('bcd-list')


# class CreateNewPR(CreateView):
# 	form_class=PRModelForm
# 	model=PR
# 	template_name='PR_form.html'

# 	def get_context_data(self,**kwargs):
# 	 	context = super().get_context_data(**kwargs)
# 	 	context['BCD_no']=self.kwargs['string']
# 	 	return context

# 	def form_valid():
# 		pass

def generate_pdf(request, pk):
	PR_No=PR.objects.get(id=pk).PR_No
	title = str(PR_No)
	filename = title + ".pdf"
	response = HttpResponse(content_type='text/pdf')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	def pdf_rdm1(file_name):
	    from fpdf import FPDF
	    class PDF1(FPDF):
	        FPDF.orientation = 'L'

	        def header(self):
	            #self.image(settings.BASE_DIR + '\\static\\img\\rbl.jpg', x=10, y=12, w=50).replace("/", "\\")
	            self.set_font('Arial', 'B', 12)
	            # Calculate width of title and position
	            pr = PR.objects.get(PR_No=PR_No)
	            requestor_id = 'BCDUser'
	            w = self.get_string_width(title) + 6
	            col1 = (180 - self.get_string_width(title) + 6) / 2
	            title2 = 'BCD No. : ' + str(pr.BCD_no)
	            col2 = (275 - w - self.get_string_width(title2) + 6) / 2
	            self.set_text_color(128)

	            # Header Line 1
	            # Title 1
	            self.set_x(col1)
	            self.cell(col1, 9, 'BCD No. : ' + str(pr.BCD_no), 0, 1, 'L')
	            # Title 2
	            title2 = 'Bussiness : ' + str(pr.Business)
	            self.set_x(col2)
	            self.cell(col2, -9, title2, 0, 1, 'R')

	            # Header Line 2
	            # Title 1
	            title1 = 'PR No. : ' + str(pr.PR_No)
	            self.set_x(col1)
	            self.cell(col1, 20, title1, 0, 1, 'L')
	            # Title 2
	            title3 = 'Start Date : ' + str(pr.start_date)
	            self.set_x(col2)
	            self.cell(col2, -20, title3, 0, 1, 'R')

	            # Header Line 3
	            # Title 1
	            title1 = 'Budget : ' + str(pr.Budget)
	            self.set_x(col1)
	            self.cell(col1, 30, title1, 0, 1, 'L')
	            # Title 2
	            title3 = 'End Date : ' + str(pr.end_date)
	            self.set_x(col2)
	            self.cell(col2, -30, title3, 0, 1, 'R')

	            self.ln(25)

	        def footer(self):
	            # Position at 1.5 cm from bottom
	            self.set_y(-40)
	            epw = self.w - 2 * self.l_margin
	            col_width = epw / 8
	            self.set_font('Times', 'B', 10.0)
	            self.ln(0.5)
	            th = self.font_size
	            self.cell(col_width, 2 * th, '1st App', border=1)
	            self.cell(col_width+8, 2 * th, 'CEO', border=1)
	            self.cell(col_width+8+8, 2 * th, '', border=1)

	            self.ln(2 * th)
	            self.cell(col_width, 2 * th, '2nd App', border=1)
	            self.cell(col_width+8, 2 * th, 'Finance', border=1)
	            self.cell(col_width+8+8, 2 * th, '', border=1)

	            self.ln(2 * th)
	            self.cell(col_width, 2 * th, '3rd App', border=1)
	            self.cell(col_width+8, 2 * th, 'CIO', border=1)
	            self.cell(col_width+8+8, 2 * th, '', border=1)

	            self.set_y(-15)
	            self.set_font('Arial', 'I', 8)
	            self.set_text_color(128)
	            # Page number
	            self.cell(0, 10, 'Page ' + str(self.page_no()) + ' of ' + str(self.alias_nb_pages()), 0, 0, 'C')

	        def chapter_title(self, label):
	            self.set_font('Arial', '', 12)
	            self.set_fill_color(200, 220, 255)
	            self.cell(0, 6, '%s' % (label), 0, 1, 'C', 1)
	            self.ln(4)

	        def chapter_body(self, data):
	            epw = self.w - 2 * self.l_margin
	            col_width = epw / 8
	            self.set_font('Times', 'B', 10.0)
	            self.ln(0.5)
	            th = self.font_size
	            for row in data:
	                for datum in row:
	                    self.cell(col_width, 2 * th, str(datum), border=1)
	                self.ln(2 * th)
	                # if str(row[-1]) != 'Comment':
	                # self.multi_cell(col_width * 2, 2 * th, str(row[-1]), border=1)
	                # self.ln(th)
	                self.set_font('Times', '', 10.0)
	            self.ln(th)
	            self.set_font('Times', 'B', 14.0)

	        def print_chapter(self):
	            l = PR.objects.get(PR_No=PR_No)
	            pr_grid = l.Grids.all()
	            vender_data = []
	            av1 = ''
	            vender_stamp = {}
	            vendor_name = ''
	            main_list = []
	            sub_list = []
	            sub_list = [['Item Description', 'Qty.','V1 Name','V1 Bid Amt','V2 Name','V2 Bid Amt','V3 Name','V3 Bid Amt']]

	            main_list.append(str(PR_No))
	            for pg in pr_grid:
	            	sub_list.append([pg.Item_Description,pg.Quantity,pg.Vendor_1,pg.Bid_1,pg.Vendor_2,pg.Bid_2,pg.Vendor_3,pg.Bid_3])

	            main_list.append(sub_list)
	            vender_data.append(main_list)

	            self.add_page()
	            self.ln(2)
	            for vender_document in vender_data:
	                self.chapter_title(vender_document[0])
	                self.chapter_body(vender_document[1])
	                self.ln(4)

	            main_list1 = []
	            vender_data1 = []
	            sub_list1 = []
	            sub_list1 = [['old_unit_rate','new_unit_rate','vendor_type','procurement_type','Budget_code','Tech_spoc','Start_date','End_date']]

	            main_list1.append(str(PR_No))
	            for pg in pr_grid:
	            	sub_list1.append([pg.old_unit_rate,pg.new_unit_rate,pg.vendor_type,pg.procurement_type,pg.Budget_code,pg.Tech_spoc,l.start_date,l.end_date])
	            main_list1.append(sub_list1)
	            vender_data1.append(main_list1)

	            for vender_document in vender_data1:
	                self.chapter_body(vender_document[1])
	                self.ln(4)
	            set_x_to = 10
	            ind = 1
	            self.set_font('Times', '', 10.0)

	    mypdf = PDF1(orientation = 'L', unit = 'mm', format='A4')
	    mypdf.set_title(title)
	    mypdf.set_author('RBL Bank')
	    # vc = VendorComments.objects.all()
	    mypdf.print_chapter()
	    mypdf.output(settings.BASE_DIR + '/static/download/' + filename, 'F')
	    return settings.BASE_DIR + '/static/download/' + filename

	# Above code with generatethe PDF File

	we_have_pdf = settings.BASE_DIR + '/static/download/' + filename
	pdf_rdm1(we_have_pdf)
	input = PdfFileReader(open(we_have_pdf, 'rb'))
	output = PdfFileWriter()

	for x in range(0, input.getNumPages()):
	    page1 = input.getPage(x)
	    output.addPage(page1)

	outputStream = response
	output.write(response)
	outputStream.close()

	return response


def download(request, path,filename):
    print(request.get_full_path())
    # fname = find_between(request.get_full_path(), '/docs/docs/', '.') 
    full_path=request.get_full_path()
    fname=full_path[11:]
    print('yeee..'+fname)
    fobj = BCD.objects.get(pdf='docs/' + fname)
    filename = fobj.pdf.name.split('/')[-1]
    print('fobj name '+ filename)
    # print('fobj pdf '+fobj.pdf)
    response = HttpResponse(fobj.pdf, content_type='text/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


