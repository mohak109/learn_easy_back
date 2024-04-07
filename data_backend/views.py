from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import Student, Teacher, Course, UserCred, StudentCourse
# from django.core.serializers import serialize

# Create operations
@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usercred = UserCred.objects.create(
            username=data.get('username'),
            password=data.get('password'),
            role=data.get('role')
        )
        student = Student.objects.create(
            name=data.get('name'),
            email=usercred,  # Assign the usercred instance here
            contact_no=data.get('contact_no'),
            dob=data.get('dob'),
            gender=data.get('gender'),
            discipline=data.get('discipline')
        )
        # serialized_student = serialize('json', [student])
        return JsonResponse({'message': 'Student created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed, unable to create student'})
    

@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usercred = UserCred.objects.create(
            username=data.get('username'),
            password=data.get('password'),
            role=data.get('role')
        )
        teacher = Teacher.objects.create(
            name=data.get('name'),
            email=usercred,
            dob=data.get('dob'),
            gender=data.get('gender'),
            qualification=data.get('qualification'),
            whatsapp_number=data.get('whatsapp_number')
        )
        # serialized_student = serialize('json', [student])
        return JsonResponse({'message': 'Teacher created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed, unable to create teacher'})
    

@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        teacher_id = data.get('teacher_id')  # Assuming 'teacher_id' is provided in the request body to link to a teacher
        teacher = Teacher.objects.get(pk=teacher_id)
        course = Course.objects.create(
            course_name=data.get('course_name'),
            type=data.get('type'),
            fees=data.get('fees'),
            teacher=teacher
        )
        return JsonResponse({'message': 'Course created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
    

@csrf_exempt
def create_studentcourse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_id = data.get('student_id')
        student = Student.objects.get(pk=student_id)
        course_id = data.get('course_id')
        course = Course.objects.get(pk=course_id)
        student_course = StudentCourse.objects.create(
            student=student,
            course=course,
            enrollment_date=data.get('enr_date'),
        )
        return JsonResponse({'message': 'StudentCourse created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
    
@csrf_exempt
def getOneUserCred(request):
    if request.method == 'GET':
        email = request.GET.get('email')  # Get email from request query parameters
        if email:
            try:
                usercred = UserCred.objects.get(username=email)  # Assuming email is stored as username in UserCred
                # Serialize usercred data
                usercred_data = {
                    'username': usercred.username,
                    'password': usercred.password,
                    'role': usercred.role
                }
                return JsonResponse(usercred_data)
            except UserCred.DoesNotExist:
                return JsonResponse({'error': 'UserCred not found for the provided email'}, status=404)
        else:
            return JsonResponse({'error': 'Email parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    
def findOneStudent(request):
    if request.method == 'GET':
        # data = json.loads(request.body)
        user = request.GET.get('email')
        try:
            student = Student.objects.get(email_id=user)
            student_data = {
                'name': student.name,
                'email': student.email_id,
                'contact_no': student.contact_no,
                'dob': student.dob,
                'gender': student.gender,
                'discipline': student.discipline
            }
            return JsonResponse(student_data)
        except:
            return JsonResponse({'error': 'Student not found for the provided email'}, status=404)

        # returnData = {'username':usercred.username, 'password':usercred.password, 'role':usercred.role}
        # print(usercred)
        # return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")