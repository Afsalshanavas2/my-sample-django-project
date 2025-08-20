from django.http import JsonResponse
from django.shortcuts import render
from .models import Teachers 

def products(request):
    return render(request, 'products.html')

def teacher_list(request):
    teachers = Teachers.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def search_teachers(request):
    query = request.GET.get('q', '')
    teachers = Teachers.objects.filter(tname__icontains=query)
    results = [
        {
            "name": t.tname,
            "subject": getattr(t, "tsubject", ""),
            "contact": getattr(t, "contact", "")
        }
        for t in teachers
    ]
    return JsonResponse(results, safe=False)

# Create your views here.
