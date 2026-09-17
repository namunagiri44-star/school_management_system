from django.shortcuts import render, get_object_or_404
from .models import Student, Teacher, Staff

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'staff_count': Staff.objects.count(),
    }
    return render(request, 'school_app/home.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'school_app/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school_app/student_detail.html', {'student': student})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school_app/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'school_app/teacher_detail.html', {'teacher': teacher})

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'school_app/staff_list.html', {'staff_members': staff_members})

def staff_detail(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    return render(request, 'school_app/staff_detail.html', {'staff_member': staff_member})