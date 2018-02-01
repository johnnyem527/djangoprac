from django.conf.urls import url
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index_2, name='index_2'),
    url(r'^index3/', views.index_3, name='index_3'),
    url(r'^users/', views.user_page, name='user_page'),
    url(r'^login/', views.login_page, name='form_page'),
    url(r'^signin/', views.users, name='users'),
    url(r'^home/', views.home, name='home'),
    url(r'^other/', views.other, name='other'),
    url(r'^relative/', views.relative, name='relative'),
    url(r'^register/', views.register, name='register'),

]