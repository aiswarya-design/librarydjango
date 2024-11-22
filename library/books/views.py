from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from books.models import Book
from django.template.defaultfilters import title


# Create your views here.
def home(request):
    # context={'name':'Paru','age':25}
    return render(request,'home.html')
# @login_required()
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']
        image=request.FILES['image']
        y=request.FILES['y']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,image=image,y=y)
        b.save()
        return view(request)
    return render(request,'add_books.html')
# def view(request):
#     k=Book.objects.all()
#     context={'book':k}
#     return render(request,'view_books.html',context)
# @login_required()
def view(request):
    k=Book.objects.all()
    return render(request,'view_books.html',{'book':k})




@login_required()
def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})
@login_required()
def delete(request,m):
    k=Book.objects.get(id=m)
    k.delete()
    return view(request)

@login_required()
def edit(request,p):
    k=Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.pages=request.POST['pa']
        k.language=request.POST['l']
        if(request.FILES.get('image')==None):
            k.save()
        else:
            k.c=request.FILES.get('i')

        if(request.FILES.get('i')== None):
            k.save()
        else:
            k.pdf = request.FILES['y']
        k.save()
        return view(request)
    return render(request,'edit.html',{'book':k})

from django.db.models import Q
def search_books(request):
    k=None
    query=""
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query ))


    return render(request,'search.html',{'book':k})
