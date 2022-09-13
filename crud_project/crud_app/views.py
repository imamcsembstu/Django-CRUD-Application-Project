from django.shortcuts import render
from crud_app import forms
from crud_app.models import Student

def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {'title': "Index", 'list_Of_student' : student_list}
    return render(request, 'crud_app_templates/index.html', context=diction)


def student_form(request):
    form = forms.StudentForm()
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {"title":"Student_Form", "student_form":form}
    return render(request, 'crud_app_templates/student_form.html', context=diction)

def student_info(request,student_id):
    student_info =Student.objects.get(pk=student_id)
    diction = {'title': "Student Info",'student_info':student_info}
    return render(request, 'crud_app_templates/student_info.html', context=diction)

def student_update(request,student_id):
    student_info =Student.objects.get(pk=student_id)
    form = forms.StudentForm(instance=student_info)
    if request.method =="POST":
        form=forms.StudentForm(request.POST , instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title': "Student Update",'student_form':form}
    return render(request, 'crud_app_templates/student_update.html', context=diction)


def student_delete(request,student_id):
    student =Student.objects.get(pk=student_id).delete()
    diction = {'title': "Student Delete",'delete_message':'Delete Done'}
    return render(request, 'crud_app_templates/student_delete.html', context=diction)


