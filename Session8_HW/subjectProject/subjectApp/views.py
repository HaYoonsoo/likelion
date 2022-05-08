from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView, ListView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
  model = Subject
  context_object_name = 'subjects'
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    context.update({
        'subjects': Subject.objects.all(),
        'majors': Major.objects.all(),
    })
    return context


class AddMajorView(CreateView):
  model = Major
  form_class = MajorModelForm
  template_name = 'addMajor.html'
  success_url = reverse_lazy('home')


class EditMajorView(UpdateView):
  model = Major
  form_class = MajorModelForm
  template_name = 'editMajor.html'
  success_url = reverse_lazy('home')


class AddSubjectView(CreateView):
  model = Subject
  form_class = SubjectModelForm
  template_name = 'addSubject.html'
  success_url = reverse_lazy('home')


class EditSubjectView(UpdateView):
  model = Subject
  form_class = SubjectModelForm
  template_name = 'editSubject.html'
  success_url = reverse_lazy('home')


def home(request):
    return render(request, 'home.html', {'majors': Major.objects.all(), 'subjects': Subject.objects.all()})


class FilterView(ListView):
  model = Subject
  context_object_name = 'subjects'
  template_name = 'filter.html'
  
  def get_context_data(self, **kwargs):
    print(self.kwargs['name'])
    context = super(FilterView, self).get_context_data(**kwargs)
    filtered_subjects = []
    for subject in Subject.objects.all():
      if subject.major.name == self.kwargs['name']:
        filtered_subjects.append(subject)
    context['filtered_subjects'] = filtered_subjects
    context['major_name'] = self.kwargs['name']
    return context
    

def deleteMajor(request, major_pk):
  Major.objects.get(pk=major_pk).delete()
  return redirect('home')


def deleteSubject(request, subject_pk):
  Subject.objects.get(pk=subject_pk).delete()
  return redirect('home')
