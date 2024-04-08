from django.db import models

class UserCred(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.OneToOneField(UserCred, on_delete=models.CASCADE, related_name='student', primary_key=True)
    # email = models.EmailField(unique=True, primary_key=True)
    contact_no = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    discipline = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.OneToOneField(UserCred, on_delete=models.CASCADE, related_name='teacher', primary_key=True)
    # email = models.EmailField(unique=True, primary_key=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_name

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # You can add additional fields specific to the relationship if needed
    # For example:
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"
