
# Create your views here.
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import School, Student,User
from django.contrib.auth import authenticate, login
import json



last_deleted_school_id = None

@csrf_exempt
def create_school(request):
    global last_deleted_school_id

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            required_fields = ['school_id', 'school_name', 'address', 'phone']
            school_id = data.get('school_id')

            # Validate school_id format
            if not school_id or not (school_id.startswith('A') and len(school_id) == 4):
                return JsonResponse({'error': 'Invalid school_id format. School ID should start with "A" followed by 3 digits (e.g., A001)'}, status=400)

            # Check if school_id already exists
            if School.objects.filter(school_id=school_id).exists():
                return JsonResponse({'error': f'School ID {school_id} already exists'}, status=400)

            # Check if school_id was last deleted
            if school_id == last_deleted_school_id:
                return JsonResponse({'error': f'School ID {school_id} was recently deleted and cannot be reused'}, status=400)

            school = School.objects.create(**data)
            return JsonResponse({'message': 'school created successfully'}, status=201)

            # last_deleted_school_id = None  # Reset last_deleted_school_id after successful creation
            # return JsonResponse({'message': 'School created successfully', 'school_id': school.school_id}, status=201)

        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ['student_id', 'name', 'email', 'dob', 'gender', 'school_id']
            if not all(field in data for field in required_fields):
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            student = Student.objects.create(**data)
            return JsonResponse({'message': 'Student created successfully'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    

@csrf_exempt

def delete_school(request, school_id):
    if request.method == 'DELETE':
            school = School.objects.get(school_id=school_id)
            school.delete()
            return JsonResponse({'message': 'School deleted successfully'}, status=204)
    
@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'DELETE':
            student = Student.objects.get(student_id=student_id)
            
            # Check permissions
            if request.user.role == 'admin' or student.school == request.user.school:
                student.delete()
                return JsonResponse({'message': 'Student deleted successfully'}, status=204)
            else:
                return JsonResponse({'error': 'Permission denied'}, status=403)
        
    
@csrf_exempt
def update_student(request, student_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        student = Student.objects.get(student_id=student_id)
        if request.user.role == 'admin' or student.school == request.user.school:
                # Update fields if present in request data
                if 'name' in data:
                    student.name = data['name']
                if 'email' in data:
                    student.email = data['email']
                if 'dob' in data:
                    student.dob = data['dob']
                if 'gender' in data:
                    student.gender = data['gender']
                
                student.save()
                
                return JsonResponse({'message': 'Student updated successfully'}, status=200)
        
        else:
                return JsonResponse({'error': 'Permission denied'}, status=403)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    
@csrf_exempt
def get_students_by_school(request, school_id):
        school = School.objects.get(school_id=school_id)
        students = Student.objects.filter(school=school)
        students_data = []
        for student in students:
            student_info = {
                'student_id': student.student_id,
                'name': student.name,
                'email': student.email,
                'dob': student.dob.strftime('%Y-%m-%d'), 
                'gender': student.gender,
                'school_name': student.school.school_name 
            }
            students_data.append(student_info)
        return JsonResponse(students_data, safe=False)


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        required_fields = ['username', 'phone', 'email', 'password', 'role']
        
        # if not all([user_name, phone, email, password]):
        #     return JsonResponse({'error': 'Missing required fields'}, status=400)
        
        user = User.objects.create(**data)
        return JsonResponse({'message': 'User created successfully'}, status=201)




            

@csrf_exempt
def get_schools_with_students(request):
        schools = School.objects.all()
        schools_data = []
        for school in schools:
            students = Student.objects.filter(school=school)
            students_info = []
            for student in students:
                student_info = {
                    'student_id': student.student_id,
                    'name': student.name,
                    'email': student.email,
                    'dob': student.dob.strftime('%Y-%m-%d'), 
                    'gender': student.gender,
                }
                students_info.append(student_info)

            school_info = {
                'school_id': school.school_id,
                'school_name': school.school_name,
                'address': school.address,
                'phone': school.phone,
                'students': students_info
            }
            schools_data.append(school_info)

        return JsonResponse(schools_data, safe=False)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            student_id=data.get('student_id')

            user=User.objects.filter(email=email).values().get()
 
            if User.objects.filter(email=email):
                if user["role"] == "admin":
                    student=list(Student.objects.filter(student_id=student_id).values())
 
                    if len(student)!=0:
                        delete_student=Student.objects.get(student_id=student_id)
                        delete_student.delete()
                        print("Admin longed in")
                        return JsonResponse({'message': 'Student deleted successfully'}, status=200)

                else:
                    student_info = Student.objects.filter(student_id=student_id).values()
                    return JsonResponse({'message': 'User logged in ', 'student_info': list(student_info)}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

