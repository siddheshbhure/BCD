"""BCD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from BCDApp import views
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', views.LoginView, name='login'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^logoutpage/$', views.logoutpage, name='logoutpage'),
    url(r'^dashboard/$', views.DashboardView, name='dashboard'),
    url(r'^bcd-list/$', views.bcdListView, name='bcd-list'),
    url(r'^new-bcd/$', views.CreateNewBCD.as_view(), name='new-bcd'),
    url(r'^new-bcd-COE/$', views.CreateNewBCDCOE.as_view(), name='new-bcd'),
    url(r'^docs/(?P<filename>[-\w]+)', views.download, {'path': 'docs'}, name='download'),
    url(r'^BCD/(?P<pk>[0-9]+)/$', views.UpdateBCD.as_view(), name='BCD-update'),
    url(r'^BCD-COE/(?P<pk>[0-9]+)/$', views.UpdateBCDCOE.as_view(), name='BCD-COE'),
    url(r'^BCD-FIN/(?P<pk>[0-9]+)/$', views.UpdateBCDFIN.as_view(), name='BCD-FIN'),
    url(r'^BCD-CIO/(?P<pk>[0-9]+)/$', views.UpdateBCDCIO.as_view(), name='BCD-CIO'),
    url(r'^BCD-GOV/(?P<pk>[0-9]+)/$', views.UpdateBCDFinal.as_view(), name='BCD-GOV'),
    url(r'^bcd-list-COE/$', views.bcdListCOEView, name='bcd-list-COE'),
    url(r'^bcd-list-FIN/$', views.bcdListFINView, name='bcd-list-FIN'),
    url(r'^bcd-list-CIO/$', views.bcdListCIOView, name='bcd-list-CIO'),
    url(r'^bcd-list-Final/$', views.bcdListFinalView, name='bcd-list-Final'),
    # url(r'^new-pr/(?P<string>[\w\-]+)/$', views.CreateNewPR.as_view(), name='new-pr'),
    url(r'^new-pr/(?P<string>[\w\-]+)/$', views.PRMemberCreate.as_view(), name='new-pr'),
    url(r'^PR/(?P<string>[\w\-]+)/(?P<pk>[0-9]+)/(?P<fl>[0-9]+)/$', views.PRMemberUpdate.as_view(), name='view-pr'),
    url(r'^bcd-pr/download/(?P<pk>[-\w]+)/$', views.generate_pdf, name='generate-pdf'),
]
