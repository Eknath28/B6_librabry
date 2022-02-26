from django.http import HttpResponse

def view_a(request):
    return HttpResponse('in view_a')

def view_b(request):
    return HttpResponse('in view_b')