from django.contrib import admin
from .models import  Vendor, Food, VendorAdmin
# Register your models here.

#把要管理類別加到要管理的後面 
#admin.site.register(Vendor,VendorAdmin)
#有用 @admin.register(tablename) 就不用寫了


#admin.site.register(Food)
