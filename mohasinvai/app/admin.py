from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Debit),
admin.site.register(Credit),
admin.site.register(Closing),
admin.site.register(Opaning),