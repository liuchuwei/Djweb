from django.shortcuts import render

def Hello(request):
    context = {}
    context['hello'] = "Hello world !"
    return render(request, 'runoob.html', context)