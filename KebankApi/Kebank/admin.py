from django.contrib import admin
from .models import *

admin.site.register(LegalPerson)
admin.site.register(JuridicPerson)
admin.site.register(Account)
admin.site.register(User)
admin.site.register(Address)

# Register your models here.