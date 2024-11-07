from django.shortcuts import render,get_object_or_404
from .models import Teachers,Core,Cours_comment,Roles
from .forms import ContactForm,Coursform
from django.http import FileResponse, Http404



# Create your views here.
def homepage(request):
    teacher = Teachers.objects.all()
    cours = Core.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            form.clean()
            print("lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala")
            # form = ContactForm()
    context = {
        "teacher":teacher,
        "cours":cours,
        "form":form
    }
    return render(request,'home/home-4.html',context)

def details(request,id):
    Object = get_object_or_404(Core,id=id)
    form = Coursform()
    if request.method == "POST":
        form = Coursform(request.POST)
        if form.is_valid():
            form.save()
            print("lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala")
            # form = Coursform()
            
    comment_text = Cours_comment.objects.all()
    context = {
        'object':Object,
        'form':form,
        'command':comment_text,
    }
    return render(request,"home/course-detail.html",context)

def instructor(request, id):
    teacher = get_object_or_404(Teachers, id=id)  
    roles = Roles.objects.filter(connect=teacher) 

    if not roles.exists():
        return render(request, "home/instructor-detail.html", {'roles': "role not exist"})

    context = {
        'information': teacher,
        'roles': roles,
    }
    return render(request, "home/instructor-detail.html", context)


def download_file(request, file_id):
    try:
        document = get_object_or_404(Teachers,id=file_id)
        return FileResponse(document.resume, as_attachment=True, filename=f"{document.resume.name}.pdf")
    except Teachers.DoesNotExist:
        raise Http404("File not found")