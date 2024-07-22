from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import StudentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})
