from django.contrib import admin
from .models import Ship,Client,Factory,Service,Seaport
# Register your models here.
admin.site.register(Seaport)
admin.site.register(Ship)
admin.site.register(Client)
admin.site.register(Factory)
admin.site.register(Service)
