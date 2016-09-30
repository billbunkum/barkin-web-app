from django.shortcuts import render

def splash(request):
    return render(request, "barks/global_barks_list.html")