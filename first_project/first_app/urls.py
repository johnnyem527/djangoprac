from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index_2, name='index_2'),
    url(r'^index3/', views.index_3, name='index_3'),
    url(r'^users/', views.user_page, name='user_page')
]