from django.shortcuts import render
from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from . import models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'cbv_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC Injection!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # default context_object_name is school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv_app/school_detail.html'
    # #default context_object_name = 'school'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    # default template_name = school_form.html
    # default context_object_name = 'school'

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    models = models.School

    # 不知道有什么用？但是必须要写
    def get_queryset(self):
        return models.School.objects.all()
    #default template_name = school_update_form.html
    # default context_object_name = 'school'

class SchoolDeleteView(DeleteView):
    models = models.School
    success_url = reverse_lazy("cbv_app:list")

    # 不知道有什么用？但是必须要写
    def get_queryset(self):
        return models.School.objects.all()
    #default template_name = school_confirm_delete.html
    #default context_object_name = 'school'



























