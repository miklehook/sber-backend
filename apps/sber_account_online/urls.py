from django.conf.urls import url

from apps.sber_account_online.views.view_client import ClientListView
from apps.sber_account_online.views.view_org import OrganizationListView
from apps.sber_account_online.views.view_orgtype import OrgTypeListView

urlpatterns = [

    url(r'^client/list/$', ClientListView.as_view()),
    url(r'^org/list/$', OrganizationListView.as_view()),
    url(r'^orgtype/list/$', OrgTypeListView.as_view()),

]
