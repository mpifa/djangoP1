from django.contrib import admin

from main.models import Joc
from main.models import Platform
from main.models import Company
from main.models import Type

admin.site.register(Joc)
admin.site.register(Platform)
admin.site.register(Company)
admin.site.register(Type)