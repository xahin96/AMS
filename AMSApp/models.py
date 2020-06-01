from django.db import models

request_types = (
    ('0', '---Select---'),
    ('1', 'SRS'),
    ('2', 'CR'),
    ('3', 'BRS'),
    ('4', 'Database Server Access'),
    ('5', 'Application Server Access'),
    ('6', 'Port'),
    ('7', 'IP'),
    ('8', 'Whitelisting'),
    ('9', 'Application Access'),
    ('10', 'Deployment'),
    ('11', 'Data Backup'),
)
yes_or_no = (
    ('0', 'No'),
    ('1', 'Yes'),
)
roles = (
    ('0', 'Developer'),
    ('1', 'Tester'),
)


class ApprovalRequest(models.Model):
    request_type = models.CharField(max_length=256, choices=request_types, default='0')
    request_title = models.CharField(max_length=256)
    requester = models.CharField(max_length=256)
    request_date = models.DateTimeField(blank=True, null=True)
    required_date = models.DateTimeField(blank=True, null=True)
    purpose = models.TextField(blank=True, default='')
    ip_required = models.CharField(max_length=256, choices=yes_or_no, default='0')
    user_required = models.CharField(max_length=256, choices=yes_or_no, default='0', blank=True)
    name = models.CharField(max_length=256, blank=True)
    role = models.CharField(max_length=256, choices=roles, blank=True)
    database_required = models.CharField(max_length=256, choices=yes_or_no, default='0', blank=True)

    def __str__(self):
        return f"{str(self.pk)} - {self.request_type} - {self.request_title}"


class IPInformation(models.Model):
    ip_address = models.CharField(max_length=256, blank=True)
    port = models.CharField(max_length=256, blank=True)
    approval_request = models.ForeignKey(
        ApprovalRequest,
        related_name='ip_informations',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    def __str__(self):
        return f"{str(self.pk)} - {self.ip_address} - {self.port}"


class ApprovalRequestFiles(models.Model):
    file = models.FileField(blank=True, null=True)
    approval_request = models.ForeignKey(
        ApprovalRequest,
        related_name='files',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    def __str__(self):
        return f"{str(self.pk)}"
