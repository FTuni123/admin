from django.contrib import admin
from .models import *
#CompanyBank, EmployeeBank


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Bill)
admin.site.register(BillDetails)
