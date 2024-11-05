from django.urls import path
from .views import homepage,details,instructor,download_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",homepage,name="home"),
    path("course-detail/<int:id>",details,name="course-detail"),
    path("information/<int:id>",instructor,name="instructor-detail"),
    path("download/<int:file_id>",download_file,name="resume")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)