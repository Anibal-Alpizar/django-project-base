from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h3>Hello world</h3>")

def about(request):
    return HttpResponse("About")

