from django import forms
from .models import Contactus,Cours_comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ["name","email","service","message"]
        
        widgets = {
            "name":forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"نام و نام خانوادگی"}),
            "email":forms.TextInput(attrs={'type':"email",'class':"form-control",'placeholder':"ایمیل"}),
            "service":forms.Select(attrs={'class':"form-control"}),
            "message":forms.Textarea(attrs={'class':"form-control",'rows':"5",'placeholder':"پیام خود را وارد کنید"}),
        }
        
class Coursform(forms.ModelForm):
    class Meta:
        model = Cours_comment
        fields = ["name","email","comment"]
        
        widgets = {
            "name":forms.TextInput(attrs={'class':"form-control",'type':"text",'placeholder':"نام و نام خانوادگی"}),
            "email":forms.TextInput(attrs={'class':"form-control",'type':"email",'placeholder':"ایمیل"}),
            "comment":forms.Textarea(attrs={'class':"form-control ht-140",'placeholder':"نظر خود را بنویسید..."})
        }