from django.contrib import admin
from .models import Core,Teachers,Contactus,Cours_comment,Roles

# Register your models here.
admin.site.register(Core)
# admin.site.register(Teachers)
admin.site.register(Contactus)
admin.site.register(Cours_comment)




class RolesInLine(admin.TabularInline):
    model = Roles
    extra = 1

@admin.register(Teachers)
class CourseAdmin(admin.ModelAdmin):
    inlines = [RolesInLine]
