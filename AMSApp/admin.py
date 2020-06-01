from django.contrib import admin
from AMSApp.models import ApprovalRequest, IPInformation, ApprovalRequestFiles


admin.site.register(ApprovalRequest)
admin.site.register(IPInformation)
admin.site.register(ApprovalRequestFiles)
