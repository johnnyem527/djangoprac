from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage, User
from . import forms
from .forms import NewUserForm, UserForm, UserProfileInfoForm
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

def login_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do Something code
            print("Validation success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form' : form})

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return user_page(request)
        else:
            print('Error Form Invalid')

    return render(request, 'first_app/users.html', {'form' : form})

def home(request):
    context_dict = {'text': 'hello world',
                    'number': 100}

    return render(request, 'first_app/home.html', context=context_dict)

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {'user_form' : user_form,
                                                           'profile_form' : profile_form,
                                                           'registered': registered})















