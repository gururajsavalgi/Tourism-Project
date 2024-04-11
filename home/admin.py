from django.contrib import admin




# Register your models here.
from .models import Index, Contact,Customer_detail,Guide_detail

admin.site.register(Contact)
admin.site.register(Index)
admin.site.register(Customer_detail)
admin.site.register(Guide_detail)


