from django.contrib import admin

# Register your models here.
from apps.sber_account_online.models.model_client import Client
from apps.sber_account_online.models.model_org import Organization
from apps.sber_account_online.models.model_orgtype import OrgType


class OrgTypeAdmin (admin.ModelAdmin):
    list_display = ('short_name','full_name',)

class OrganisationAdmin (admin.ModelAdmin):
    list_display = ('INN','OGRN')

class ClientAdmin (admin.ModelAdmin):
    list_display = ('FIO',)



admin.site.register(OrgType, OrgTypeAdmin)
admin.site.register(Organization, OrganisationAdmin)
admin.site.register(Client, ClientAdmin)

