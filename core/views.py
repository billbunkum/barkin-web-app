from django.shortcuts import render

def splash(request):
    return render(request, "core/index.html")