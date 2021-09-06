from django.urls import path
from .views import *



urlpatterns =[
    path('adobe-login/',adobe_login,name='adobe-login'),
    path('principal-list/',get_principal_list,name='adobe'),
    path('common-info/',get_common_info,name='common-info'),
    path('report-bulk-users/',report_bulk_users,name='report-bulk-users'),
]