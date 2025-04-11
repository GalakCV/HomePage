from django.shortcuts import render

def RenderMainPage(request):
    return render (request, 'main/main.html')