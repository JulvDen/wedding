from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Family, FamilyMember

admin.site.register(Family)


class FamilyMemberAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'toCeremony', 'toReception', 'toDinner','toParty', 'family']


admin.site.register(FamilyMember, FamilyMemberAdmin)