from django.shortcuts import render

def index(request):
    return render(request, "barks/global_barks_list.html")