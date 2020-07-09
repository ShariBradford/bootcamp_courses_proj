from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request,'courses.html', context)

def create_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors: 
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('/')
        
    else:
        Course.objects.create(
            name=request.POST["name"], 
            desc=Description.objects.create(desc=request.POST["desc"])
        )
        return redirect("/")

def destroy_course(request,course_id):
    this_course = Course.objects.get(id=course_id)
    context = {
        "id": this_course.id,
        "name": this_course.name,
        "desc": this_course.desc.desc,
        "created_at": this_course.created_at,
    }
    return render(request, 'delete.html',context)

def delete_course(request,course_id):
    if request.POST['do_delete'] == "True":
        this_course = Course.objects.get(id=course_id)
        this_description = Description.objects.get(id=this_course.desc.id)
        this_description.delete()
        this_course.delete()
    return redirect('/')

def show_comments(request,course_id):
    context = {
        "course":  Course.objects.get(id=course_id),
        "comments": Comment.objects.filter(course_id = course_id),
    }
    return render(request,'comments.html', context)

def add_comment(request,course_id):
    errors = Comment.objects.basic_validator(request.POST)
    if errors: 
        for k,v in errors.items():
            messages.error(request,v)
        return redirect(f"courses/{course_id}/comments")
        
    else:
        Comment.objects.create(
            course=Course.objects.get(id=course_id),
            content=request.POST["content"], 
        )
        return redirect(f"courses/{course_id}/comments")

