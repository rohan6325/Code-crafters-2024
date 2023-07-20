from django.shortcuts import render
from django.http import HttpResponse
from .models import post
posts =[
    {
        'author': 'Rohan',
        'title':'day 1',
        'content':'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available',
        'date':'today' 
        },
         {
        'author': 'Rahul',
        'title':'day 2',
        'content':'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available',
        'date':'yesterday' 
        },
         {
        'author': 'Omika',
        'title':'day 3',
        'content':'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available',
        'date':'2 days ago' 
        }
]
def home (request):
    context ={
        'posts':post.objects.all()
    }
    return render(request, 'home.html',context)
def about (request):
    return render(request, 'index.html')
