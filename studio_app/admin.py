# from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Lab)
admin.site.register(Component)
admin.site.register(Member)
admin.site.register(Source_Of_Expenses)
admin.site.register(Source_of_Income)
admin.site.register(Income)
admin.site.register(Expenses)
admin.site.register(Purchases)
admin.site.register(Member_type)
admin.site.register(Location)
admin.site.register(CheckInAndout)
admin.site.register(Request)
admin.site.register(Requestcomponents)
admin.site.register(Department)
