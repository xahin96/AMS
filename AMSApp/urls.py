from django.urls import path
from AMSApp.views import Dashboard, create_request


app_name = 'AMSApp'
urlpatterns = [
    path('a/', Dashboard.as_view(), name='dashboard'),
    # path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('create_request/', create_request, name='create_request'),
]
