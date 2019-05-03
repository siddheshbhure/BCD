from django.contrib import admin
from .models import BCD,COEHead,CIOHead,FinanceHead,GovHead,Vendor
from .forms import BCDModelForm

# Register your models here.
class COEHeadAdmin(admin.ModelAdmin):
    list_display = ['COE_ID','COE_Name','COE_Email']
    def save_model(self, request, obj, form, change):
        # obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(COEHead,COEHeadAdmin)

class CIOHeadAdmin(admin.ModelAdmin):
    list_display = ['CIO_ID','CIO_Name','CIO_Email']
    def save_model(self, request, obj, form, change):
        # obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(CIOHead,CIOHeadAdmin)


class FinanceHeadAdmin(admin.ModelAdmin):
    list_display = ['Fin_ID','Fin_Name','Fin_Email']
    def save_model(self, request, obj, form, change):
        # obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(FinanceHead,FinanceHeadAdmin)

class GovHeadAdmin(admin.ModelAdmin):
    list_display = ['Gov_ID','Gov_Name','Gov_Email']
    def save_model(self, request, obj, form, change):
        # obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(GovHead,GovHeadAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name']
    def save_model(self, request, obj, form, change):
        # obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Vendor,VendorAdmin)



# class BCDAdmin(admin.ModelAdmin):
#     # list_display = ['COE_ID','COE_Name','COE_Email']
#     form = BCDModelForm
#     def save_model(self, request, obj, form, change):
#         # obj.save()
#         super().save_model(request, obj, form, change)

# admin.site.register(BCD,BCDAdmin)

class BCDAdmin( admin.ModelAdmin ):
    form = BCDModelForm