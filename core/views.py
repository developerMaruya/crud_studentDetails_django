from django import views
from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self,request):
        stu_data=Student.objects.all()
        return render(request,'core/home.html',{'studata':stu_data})


class Add_Student(View):
    def get(self,request):
        fm=AddStudentForm()
        return render(request,'core/add-student.html',{'form':fm})

    def post(self,request):
        # ALL form data inside fm here
        fm=AddStudentForm(request.POST)
        # print(fm)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add-student.html',{'form':fm})

class Delete_Student(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        # print(id)
        studata=Student.objects.get(id=id)
        # print(studata)
        studata.delete()
        return redirect('/')
class Edit_Student(View):
    def get(self,request,id):
        stu=Student.objects.get(id=id)
        fm=AddStudentForm(instance=stu)
        return render(request,'core/edit-student.html',{'form':fm})

    def post(self,request,id):
        stu=Student.objects.get(id=id)
        # instance matlab phlai ka jo data hai usai diga and post wala new jo update kai liyai aayatha
        fm=AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')