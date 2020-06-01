from rest_framework import serializers
from AMSApp.models import ApprovalRequest, IPInformation, ApprovalRequestFiles


class ApprovalRequestFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalRequestFiles
        fields = ('file',)


class IPInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPInformation
        fields = ('ip_address', 'port')


class ApprovalRequestSerializer(serializers.ModelSerializer):
    ip_informations = IPInformationSerializer(many=True)

    class Meta:
        model = ApprovalRequest
        fields = (
            'request_type',
            'request_title',
            'requester',
            'request_date',
            'required_date',
            'purpose',
            'ip_required',
            'user_required',
            'name',
            'role',
            'database_required',
            'ip_informations',
            'files'
        )

#
# class IPInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IPInformation
#         fields = '__all__'
#
#
# class ApprovalRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApprovalRequest
#         fields = '__all__'
