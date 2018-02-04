from django.conf.urls import url
from cbv_app import views

# TEMPLATE TAGGING
app_name = 'cbv_app'

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
]