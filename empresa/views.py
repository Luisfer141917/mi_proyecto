from django.shortcuts import render

# Create your views here.
def empresa(request):
    context={
        
    }
    return render(request,"empresa/empresa.html",context)