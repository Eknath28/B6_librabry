from django.http import HttpResponse

def view_c(request):
    return HttpResponse('in view_c')

def view_d(request):
    return HttpResponse('in view_d')