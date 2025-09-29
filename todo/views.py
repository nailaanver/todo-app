from asyncio import tasks
from datetime import date, timezone
from urllib import request
from django.forms import DateField
from django.shortcuts import get_object_or_404, redirect, render


from .models import Tables

# Create your views here.
def index(request):
    mymembers = Tables.objects.all().order_by('created_date')
    today = date.today()
    return render(request,'index.html',{'mymembers': mymembers,'today':today})
def add(request):
  today = date.today()

  return render(request,'add.html',{"today" : today})

def addrecord(request):
  task= request.POST['task']
  status= request.POST['status']
  due_date = request.POST['due_date']
  status = request.POST.get('status', 'pending')
  # tdue_date = request.POST.get('due_date', None)


  new_member = Tables(task = task,status = status,due_date = due_date)
  new_member.save()
  return redirect('index')
# def delete(request):
#   member = Tables.objects.all()
#   return render(request,'delete.html',{'member':member})
# def deletemember(request,id):
#   member = get_object_or_404(Tables, id=id)
#   member.delete()
#   return redirect("index")

def delete(request, id):
    task = get_object_or_404(Tables, id=id)

    if request.method == "POST":
        task.delete()
        return redirect("index")

    return render(request, 'delete.html', {'task': task})

def update(request,id):
  member = get_object_or_404(Tables, pk=id)

       # If it's a POST request, update the member
  if request.method == 'POST':
        task_title = request.POST['task']
        tstatus = request.POST['status']
        tdue_date = request.POST['due_date']
        member.task = task_title
        member.status = tstatus
        member.due_date = tdue_date
        member.save()
        return redirect('index')
      

    # If it's a GET request, show the update form with existing data
  context = {'member': member,
             'today': date.today()}


  return render(request, 'update.html', context)






    
