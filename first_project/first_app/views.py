from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage, User
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    # my_dict = {'insert_me': 'I love Emma'}
    return render(request, 'first_app/index.html', context=date_dict)

def index_2(request):
    my_help = {'name': 'Emma Watson'}
    return render(request, 'first_app/help_page.html', context=my_help)

def index_3(request):
    return HttpResponse("<h1>My Third App</h1><hr>")

def user_page(request):
    user_list = User.objects.all()
    user_dict = {'users' : user_list}
    return render(request, 'first_app/user_page.html', context=user_dict)
