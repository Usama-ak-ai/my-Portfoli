from django.shortcuts import render,redirect
from django.http import HttpResponse
from demoapp.models import Contact
from django.contrib import messages
from demoapp import models

# Create your views here.

              
def Contact(request):
              if request.method=='POST':
                            name=request.POST.get('name')
                            email=request.POST.get('email')
                            number=request.POST.get('number')
                            content=request.POST.get('content')
                            print(name,email,number,content)
                            
                            
                            if 1<len(name)<30:
                                          pass
                            else:
                                          messages.error(request,'length of the name should be between 1 and 30')
                                          return render(request,'home.html')
                            if len (email)>1 and len(email)<30:
                                          pass
                            else:
                                          messages.error(request,'invaild email try again ')
                                          return render(request,'home.html')
                            print(len(number))
                            if  len(number)>9 and len(number)<13:
                                          pass
                            else:
                                          messages.error(request,'invaild number please try again ')
                                          return render(request,'home.html')
                            ins = models.Contact(name=name,email=email,content=content,number=number)
                            ins.save()
                            messages.success(request,'Thank You for contacting me!! Your message has been saved ')
                            print('data has been saved to database')
 
                            print('The request is no pass ')
              
              
              
              
              
              
              
              
              return render(request,'home.html')              
                            
