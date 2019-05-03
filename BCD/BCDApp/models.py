from django.db import models
import datetime

# Create your models here.
class CIOHead(models.Model):
	CIO_ID=models.CharField(max_length=30)
	CIO_Name=models.CharField(max_length=30)
	CIO_Email=models.CharField(max_length=50)

	def __str__(self):
		return self.CIO_Name

class FinanceHead(models.Model):
	Fin_ID=models.CharField(max_length=30)
	Fin_Name=models.CharField(max_length=30)
	Fin_Email=models.CharField(max_length=50)

	def __str__(self):
		return self.Fin_Name

class COEHead(models.Model):
	COE_ID=models.CharField(max_length=30)
	COE_Name=models.CharField(max_length=30)
	COE_Email=models.CharField(max_length=50)

	def __str__(self):
		return self.COE_Name

class GovHead(models.Model):
	Gov_ID=models.CharField(max_length=30)
	Gov_Name=models.CharField(max_length=30)
	Gov_Email=models.CharField(max_length=50)

	def __str__(self):
		return self.Gov_Name

class Budget(models.Model):
	budget_name=models.CharField(max_length=25)	

	def __str__(self):
		return self.budget_name

class Budget_Code(models.Model):
	budget_code=models.CharField(max_length=25)
	budget_desc=models.CharField(max_length=25)	

	def __str__(self):
		return self.budget_code

class Type_of_Expense(models.Model):
	type_of_expense=models.CharField(max_length=20)

	def __str__(self):
		return self.type_of_expense

class Vendor_Type(models.Model):
	vendor_type=models.CharField(max_length=20)

	def __str__(self):
		return self.vendor_type

class Vendor(models.Model):
	vendor_name=models.CharField(max_length=50)

	def __str__(self):
		return self.vendor_name


class Procurement_Type(models.Model):
	procurement_type=models.CharField(max_length=20)

	def __str__(self):
		return self.procurement_type

class BCD(models.Model):
	BCD_no=models.CharField(max_length=30)
	requestor_ID=models.CharField(max_length=20,default='00000')
	requestor_name=models.CharField(max_length=30)
	BCD_amount=models.CharField(max_length=8)
	BCD_summary=models.CharField(max_length=100)
	is_reffered=models.BooleanField(default=False)
	BCD_reference_no=models.CharField(max_length=30)
	FirstApproval=models.ForeignKey(COEHead,related_name='BCDs',on_delete=models.SET_NULL,verbose_name='1st Approver ',null=True)
	status=models.CharField(max_length=40,default='Pending with COE')
	pdf = models.FileField(upload_to='docs/',verbose_name='Upload BCD')
	COE_status=models.CharField(max_length=30)
	COE_Comments=models.CharField(max_length=50,null=True)
	Finance_status=models.CharField(max_length=30)
	Finance_Comments=models.CharField(max_length=50,null=True)
	CIO_status=models.CharField(max_length=30)
	CIO_Comments=models.CharField(max_length=50,null=True)
	Final_status=models.CharField(max_length=30,default='NA')
	Final_Comments=models.CharField(max_length=50,null=True)
	isPRRaised=models.BooleanField(default=False)


	def __str__(self):
		return self.BCD_no

class PR(models.Model):
	PR_No=models.CharField(max_length=30) 
	BCD_no=models.ForeignKey(BCD,related_name='PRs',on_delete=models.SET_NULL,null=True)
	Request_date=models.CharField(max_length=30)
	Application_system=models.CharField(max_length=30) 
	Budget=models.ForeignKey(Budget,related_name='Budgets',on_delete=models.SET_NULL,verbose_name='Budget',null=True)
	Business=models.CharField(max_length=30) 
	start_date=models.DateField()
	end_date=models.DateField()
	Number_of_months=models.CharField(max_length=30)

	def __str__(self):
		return self.PR_No


class PRGrid(models.Model):
	PR_No=models.ForeignKey(PR, on_delete=models.CASCADE, related_name='Grids')
	Item_Name=models.CharField(max_length=50,blank=True,null=True)
	Item_Description=models.CharField(max_length=250,blank=True,null=True)
	Quantity=models.PositiveIntegerField(default=0)
	type_of_expense=models.ForeignKey(Type_of_Expense,related_name='type_of_expenses',on_delete=models.SET_NULL,verbose_name='Type_of_Expense',null=True)
	old_unit_rate=models.DecimalField(decimal_places=2,default=0,max_digits=3)
	new_unit_rate=models.DecimalField(decimal_places=2,default=0,max_digits=3)
	vendor_type=models.ForeignKey(Vendor_Type,related_name='VendorTypes',on_delete=models.SET_NULL,verbose_name='Vendor Type',null=True)
	procurement_type=models.ForeignKey(Procurement_Type,related_name='ProcurementTypes',on_delete=models.SET_NULL,verbose_name='Procurement Types',null=True)
	Budget_code=models.ForeignKey(Budget_Code,related_name='BudgetCodes',on_delete=models.SET_NULL,verbose_name='Budget Code',null=True)
	Tech_spoc=models.CharField(max_length=50,blank=True,null=True)
	start_date=models.CharField(max_length=50,blank=True,null=True)
	end_date=models.CharField(max_length=50,blank=True,null=True)
	Vendor_1=models.CharField(max_length=50,blank=True,null=True)
	Vendor_2=models.CharField(max_length=50,blank=True,null=True)
	Vendor_3=models.CharField(max_length=50,blank=True,null=True)
	Bid_1=models.CharField(max_length=50,blank=True,null=True)
	Bid_2=models.CharField(max_length=50,blank=True,null=True)
	Bid_3=models.CharField(max_length=50,blank=True,null=True)
	

	def __str__(self):
		return self.Item_Name

