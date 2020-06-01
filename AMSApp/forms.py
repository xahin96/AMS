from django import forms
from django.forms import ModelForm
from AMSApp.models import ApprovalRequest, IPInformation
from django.utils.translation import gettext_lazy as _

yes_or_no = (
    ('0', 'No'),
    ('1', 'Yes'),
)


class ApprovalRequestForm(ModelForm):
    request_title = forms.CharField(label='')
    requester = forms.CharField(label='')
    request_date = forms.DateField(label='', widget=forms.TextInput(attrs={'type': 'date'}))
    required_date = forms.DateField(label='', widget=forms.TextInput(attrs={'type': 'date'}))
    purpose = forms.CharField(label='', widget=forms.Textarea)
    ip_required = forms.ChoiceField(
        label='',
        choices=yes_or_no,
        widget=forms.Select(attrs={'onchange': "IPRequired_Change();"})
    )
    name = forms.CharField(label='')

    class Meta:
        model = ApprovalRequest
        fields = '__all__'
        labels = {
            'request_type': _(''),
            'ip_required': _(''),
            'user_required': _(''),
            'database_required': _(''),
            'role': _(''),
        }


class IPInformationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.ip_required = kwargs.pop('ip_required', None)
        super(IPInformationForm, self).__init__(*args, **kwargs)

    ip_address = forms.CharField(label='', required=False)
    port = forms.CharField(label='', required=False)

    class Meta:
        model = IPInformation
        fields = '__all__'

    def clean_ip_address(self):
        ip_address = self.cleaned_data.get('ip_address')
        if self.ip_required == '1':
            if ip_address == '' or None:
                raise forms.ValidationError('This field can not be empty')
        return ip_address

    def clean_port(self):
        port = self.cleaned_data.get('port')
        if self.ip_required == '1':
            if port == '' or None:
                raise forms.ValidationError('This field can not be empty')
        return port
