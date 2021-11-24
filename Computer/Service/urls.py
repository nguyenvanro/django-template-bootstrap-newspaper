from django import views
from django.urls import path

from Service.views import views
from Service.views.home import view_home
from Service.views.detail import view_detail

urlpatterns = [
    path('', view_home.HomeView.as_view(), name='home'),
    path('trending/detail/', view_detail.Detail_Trending.as_view(), name='detail_top_trending'),
    path('contact', views.ContactView, name='contact_form'),
]