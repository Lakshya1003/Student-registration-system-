from django.shortcuts import render

# Create your views here.
def all_studnet(request):
    return render(request, 'student_app/all_student.html')