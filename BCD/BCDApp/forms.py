from django.forms import ModelForm, inlineformset_factory,Textarea
from django import forms

from .models import BCD,PR,PRGrid


class BCDModelForm( forms.ModelForm ):
    BCD_summary = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}))

    class Meta:
        model = BCD
        fields=['BCD_amount','FirstApproval','pdf','BCD_summary']
        # widgets={
        # 	'BCD_overview': Textarea(attrs={'cols':80,'rows':50}),
        # }


class BCDModelCOEForm( forms.ModelForm ):
    BCD_summary = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}))
    COE_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='COE Comments')
    

    class Meta:
        model = BCD
        fields=['BCD_amount','BCD_summary','FirstApproval','COE_Comments']
        # widgets={
        # 	'BCD_overview': Textarea(attrs={'cols':80,'rows':50}),
        # }


class BCDModelFINForm( forms.ModelForm ):
    BCD_summary = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}))
    COE_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='COE Comments')
    Finance_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='Finance Comments')

    class Meta:
        model = BCD
        fields=['BCD_amount','BCD_summary','FirstApproval','COE_Comments','Finance_Comments']
        # widgets={
        #   'BCD_overview': Textarea(attrs={'cols':80,'rows':50}),
        # }

class BCDModelCIOForm( forms.ModelForm ):
    BCD_summary = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}))
    COE_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='COE Comments')
    Finance_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='Finance Comments')
    CIO_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='CIO Comments')

    class Meta:
        model = BCD
        fields=['BCD_amount','BCD_summary','FirstApproval','COE_Comments','Finance_Comments','CIO_Comments']

class BCDModelFinalForm( forms.ModelForm ):
    BCD_summary = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}))
    COE_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='COE Comments')
    Finance_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='Finance Comments')
    CIO_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='CIO Comments')
    Final_Comments = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}),label='Comments')

    class Meta:
        model = BCD
        fields=['BCD_amount','BCD_summary','FirstApproval','COE_Comments','Finance_Comments','CIO_Comments','Final_Comments']

class DateInput(forms.DateInput):
    input_type = 'date'

class PRModelForm(forms.ModelForm):

        # self.firstapproval=kwargs['firstapproval']

        # self.fields['Tech_spoc'].initial='abcs'
	
	def get_form(self, request, obj=None, **kwargs):
		form = super(PRModelForm, self).get_form(request, obj=obj, **kwargs)
		form.base_fields['Tech_spoc'].initial = 'hellooo'
		return form
		
	class Meta:
		model = PR
		fields=['Application_system','Budget','Business','start_date','end_date','Number_of_months']
		widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()}

# class PRModelFormUpdate(forms.ModelForm):
#     # BCD_overview = forms.CharField( widget=forms.Textarea(attrs={'cols':35,'rows':5}))

#     class Meta:
#         model = PR
#         fields=['PR_No','Application_system','Budget','Business','start_date','end_date','Number_of_months']
        
#         widgets = {
#             'start_date': DateInput(),
#             'end_date': DateInput(),
#         }



class PRMemberForm(forms.ModelForm):    # Documents to be attached to loan application
    class Meta:
        model = PRGrid
        # exclude = ('type_of_expense','old_unit_rate','new_unit_rate','vendor_type','procurement_type','Budget_code','Tech_spoc','start_date','end_date','Vendor_1','Vendor_2','Vendor_3','Bid_1','Bid_2','Bid_3')
        exclude=()
        # widgets={'pdf':forms.ClearableFileInput()}
    
        # self.fields['my_field'].label = False
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }


PRMemberFormSet = inlineformset_factory(PR, PRGrid,form=PRMemberForm,extra=1,can_delete=False)
PRMemberFormSetView = inlineformset_factory(PR, PRGrid,form=PRMemberForm,extra=0,can_delete=False)


