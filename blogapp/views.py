
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'GET':
        print('get')
    elif request.method =='POST':
        pst=Post()
        initial={}
        name = request.POST.getlist('name')
        email = request.POST.getlist('email')
        body = request.POST.getlist('body')
        bulk_number = int(request.data.get('bulk_number'))
        
        for i in range(9):
                mmm=Post.objects.create(
                    name=name[i], email=email[i],body=body[i]
                )
                mmm.save()
                print(name[i])
                print(email[i])
                print(body[i])
                # pst.name = name[i]
                # pst.email = email[i]
                # pst.body = body[i]
                # pst.save()
    return render(request, 'multForm/index.html')



# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         print('get')
#     elif request.method =='POST':
#         pst=Post()
#         initial={}
#         name = request.POST.getlist('name')
#         email = request.POST.getlist('email')
#         body = request.POST.getlist('body')
#         print(name[0])
#         print(email[0])
#         print(body[0])
#         pst.name = name[0]
#         pst.email = email[0]
#         pst.body = body[0]
#         pst.save()
#     return render(request, 'multForm/index.html')



# def index(request):
#     if request.method == 'GET':
#         print('get')
#     elif request.method =='POST':
#         print(request.POST)
#         pst=Post()
#         pst.name = request.POST.get('name')
#         pst.email = request.POST.get('email')
#         pst.body = request.POST.get('body')
#         pst.save()
#         messages.success(request, "Form Added Successfully")
#         # return redirect('/')
#     return render(request, 'multForm/index.html')