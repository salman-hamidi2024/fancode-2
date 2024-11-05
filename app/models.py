from django.db import models
from django_jalali.db import models as jmodels
from django_resized import ResizedImageField

# Create your models here.
class Core(models.Model):
    started = jmodels.jDateField(auto_now=True)
    image = ResizedImageField(upload_to="courses",size=[348,232],scale=1,crop=["middle","center"])
    choices = [
        ("دوره تحلیلی داده","دوره تحلیلی داده"),
        ("دوره پیشرفته وب","دوره پیشرفته وب"),
        ("دوره مقدماتی برنامه نویسی","دوره مقدماتی برنامه نویسی"),
    ]
    basin = models.CharField(default="دوره تحلیلی داده",choices=choices,max_length=25)
    title = models.CharField(max_length=200)
    type_cours = [
        ('گرافیک',"گرافیک "),
        ('طراحی سایت',"طراحی سایت"),
        ('زبان برنامه نویسی','زبان برنامه نویسی'),
        ('هک و امنیت',"هک و امنیت")
    ]
    type_model = models.CharField(max_length=25,choices=type_cours,default="")
    decription = models.TextField(default="")
    hourse = models.IntegerField()
    def __str__(self):
        return self.title

class Teachers(models.Model):
    profile = ResizedImageField(upload_to="teachers",size=[368,368],scale=1,crop=["middle","center"])
    resume = models.FileField(upload_to='resume', max_length=100,default="")
    choices = [
        ('مدرس برتر ریاضی و فیزیک"',"مدرس برتر ریاضی و فیزیک"),
        ('مدرس برتر شیمی',"مدرس برتر شیمی"),
        ('دکترای آموزش زبان انگلیسی',"دکترای آموزش زبان انگلیسی"),
        ('مدرس برتر پایتون/جاوا اسکریپت',"مدرس برتر پایتون/جاوا اسکریپت"),
        ('مؤلف و مدرس شیمی کنکور',"مؤلف و مدرس شیمی کنکور")
    ]
    Expertise = models.CharField(choices=choices,default="مدرس برتر ریاضی و فیزیک",max_length=30)
    name = models.CharField(max_length=100)
    discribe = models.TextField(default="")
    
    def __str__(self):
        return self.name



class Roles(models.Model):
    connect = models.ForeignKey(Teachers,on_delete=models.CASCADE,)
    
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('js', 'JavaScript'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Go', 'Go'),
        ('swift', 'Swift'),
        ('kotlin', 'Kotlin'),
        ('ruby', 'Ruby'),
        ('php', 'PHP'),
        ('r', 'R'),
        ('typescript', 'TypeScript'),
        ('rust', 'Rust'),
        ('scala', 'Scala'),
        ('perl', 'Perl'),
        ('web', 'توسعه وب'),
        ('mobile', 'توسعه موبایل'),
        ('data science', 'علم داده'),
        ('machin learning', 'یادگیری ماشین'),
        ('game', 'توسعه بازی'),
        ('embedded', 'سیستم‌های تعبیه‌شده'),
        ('cyber', 'امنیت سایبری'),
        ('cloud', 'رایانش ابری'),
        ('iot', 'اینترنت اشیاء'),
        ('devops', 'دواپس'),
    ]
    LEVEL = [
        ('20','مبتدی'),
        ('40','متوسط'),
        ('60', 'پیشرفته'),
        ('80', 'حرفه‌ای'),
        ('100', 'استاد'),
    ]
    skill = models.CharField(max_length=150,choices=LANGUAGE_CHOICES)
    level = models.CharField(max_length=150,choices=LEVEL)


    def __str__(self):
        return self.skill


class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    choices = [
        ('site',"درخواست سایت"),
        ('work',"راه اندازی کسب و کار"),
        ('couns',"مشاوره")
    ]
    service = models.CharField(default="site",max_length=5,choices=choices)
    message = models.TextField()
    def __str__(self):
        return self.name


class Cours_comment(models.Model):
    time = jmodels.jDateField(auto_now=True)
    profile_img = models.ImageField(upload_to="comments",default="comments/b-1.png")
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.TextField()
    def __str__(self):
        return self.name