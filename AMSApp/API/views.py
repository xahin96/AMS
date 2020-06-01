from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from AMSApp.models import ApprovalRequest, IPInformation
from AMSApp.API.serializers import ApprovalRequestSerializer


@api_view(['GET','POST'])
def api_detail_approval_request_view(request):

    try:
        approval_request = ApprovalRequest.objects.all()
    except ApprovalRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApprovalRequestSerializer(approval_request, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        print('request.data')
        print(request.data)
        print('request.data')
        data_serializer = ApprovalRequestSerializer(data=request.data)

        if data_serializer.is_valid():
            try:
                a = ApprovalRequest(
                    request_type=request.data['request_type'],
                    request_title=request.data['request_title'],
                    requester=request.data['requester'],
                    request_date=request.data['request_date'],
                    required_date=request.data['required_date'],
                    purpose=request.data['purpose'],
                    ip_required=request.data['ip_required'],
                    user_required=request.data['user_required'],
                    name=request.data['name'],
                    role=request.data['role'],
                    database_required=request.data['database_required']
                )
                a.save()
                IPInformation.objects.bulk_create([IPInformation(**{'ip_address': obj['ip_address'], 'port': obj['port'], 'approval_request': a}) for obj in request.data['ip_informations']])

                return Response(data_serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response('Approval Request Creation Error', status=status.HTTP_400_BAD_REQUEST)
        return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)