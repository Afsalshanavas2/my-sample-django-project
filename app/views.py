from django.shortcuts import render
from .models import Student
from django.http import JsonResponse

def home(request):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the app goodies'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'About Page',
        'message': 'Welcome to the about page!'
    }
    return render(request, 'about.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def search_students(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(name__icontains=query)
    results = [
        {
            "name": s.name,
            "class": getattr(s, "student_class", ""),
            "division": getattr(s, "division", ""),
            "gender": getattr(s, "gender", ""),
            "contact": getattr(s, "contact", ""),
            "place": getattr(s, "place", "")
        }
        for s in students
    ]
    return JsonResponse(results, safe=False)

