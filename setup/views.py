from django.shortcuts import HttpResponse

def noadmin(request):
    return HttpResponse("Procurando algo ?")