from django.shortcuts import render,redirect
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
# Create your views here.
def show_data(request,id=None):
    instance = None
    if id:
        instance = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse("Success!!")
        else:
            return HttpResponse("Not Validated !! ")
    else:
        form = StudentForm(instance=instance)
        students = Student.objects.all()
    return render(request,'myapp/show_data.html',{'form':form,'students':students})


def delete_data(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponse("Successfully Deleted !!")
