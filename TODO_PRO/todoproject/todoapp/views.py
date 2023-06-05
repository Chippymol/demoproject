from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import form_todo
from .models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class listview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'task'
class detailview(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name = 'task2'
class updateview(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 'task_update'
    fields = ('task_name','priority','date')
    def get_success_url(self):
        return reverse_lazy('todoapp:detailview',kwargs={'pk':self.object.id})
class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:listview')



def index(request):
    taskdb = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task_name','')
        prio=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(task_name=name,priority=prio,date=date)
        task1.save()
    return render(request,'home.html',{'task':taskdb})
def delete(request,t_id):
    user=task.objects.get(id=t_id)
    if request.method=='POST':
        user.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(requets,t_id):
    task_update=task.objects.get(id=t_id)
    f=form_todo(requets.POST or None,instance=task_update)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(requets,'update.html',{'f':f,'task':task_update})

# def details(request):
#
#     return render(request,"detail.html")



