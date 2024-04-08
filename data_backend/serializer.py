from rest_framework import serializers
from .models import Student, Teacher, Course, UserCred, StudentCourse

class StuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

class TeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

class CourSerializer(serializers.ModelSerializer):
    whatsapp = serializers.CharField(source='teacher.whatsapp_number')
    name = serializers.CharField(source='teacher.name')
    disc = serializers.CharField(source='teacher.qualification')

    class Meta:
        model = Course
        fields = ['id','course_name', 'type', 'fees', 'teacher_id', 'whatsapp', 'name', 'disc']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCred
        fields = "__all__"

class StuCourSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentCourse
        fields = "__all__"