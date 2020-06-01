from django.urls import path
from AMSApp.views import Dashboard, create_request
from AMSApp.API.views import api_detail_approval_request_view


app_name = 'AMSApp.API'
urlpatterns = [
    path('', api_detail_approval_request_view, name='all'),
]
