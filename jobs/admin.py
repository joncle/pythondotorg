from django.contrib import admin

from .models import JobType, JobCategory, Job, JobContractType
from cms.admin import NameSlugAdmin, ContentManageableModelAdmin


class JobAdmin(ContentManageableModelAdmin):
    date_hierarchy = 'dt_start'
    filter_horizontal = ['job_types']
    list_display = ['__str__', 'status', 'company']
    list_filter = ['status', 'telecommuting', 'contract_type']
    raw_id_fields = ['category', 'company']


admin.site.register(JobType, NameSlugAdmin)
admin.site.register(JobCategory, NameSlugAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobContractType, NameSlugAdmin)
