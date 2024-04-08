from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addstudent", views.create_student, name="addstudent"),
    path("addteacher", views.create_teacher, name="addteacher"),
    path("addcourse", views.create_course, name="addcourse"),
    path("enrollcourse", views.create_studentcourse, name="enrollcourse"),
    path("getuser", views.getOneUserCred, name="getoneuser"),
    path('getstudent', views.findOneStudent, name='getstudent'),
    path('getcourses', views.getCoursesByType, name='getcourses'),
    path('getteacher', views.findOneTeacher, name='getteacher'),
    path('addstucourse', views.addStuCourse, name='addstucourse')
]