from django.contrib import admin

# Register your models here.

from .models import Sede, Ambiente, Instructor

admin.site.register(Sede)
admin.site.register(Ambiente)
admin.site.register(Instructor)
