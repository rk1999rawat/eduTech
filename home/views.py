from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("this")    

def contact(request):
    if request.method == "POST":
        author = request.POST['author']
        email = request.POST['email']
        subject = request.POST['subject']
        comment = request.POST['comment']
        contact=Contact(author=author, email=email, subject=subject
        )
        contact.save()

        return render(request,'contact.html', {}) 

    else:
        return render(request,'contact.html', {})


