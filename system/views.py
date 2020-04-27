from system import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializers import *
from django.views.generic import TemplateView


class Register_view(TemplateView):
    template_name = 'Registration.html'

class home_view(TemplateView):
    template_name = 'Home.html'


@api_view(['GET', 'POST'])
def UserRegister(request):
    if request.method == 'GET':
        form = forms.RegisterForm()
        print("in get")
        return render(request, 'Registration.html', {'form': form})

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print("here")
        if serializer.is_valid():
            print("valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def reg_view(request):
    if request.method == 'POST':
        form=forms.RegisterForm(data=request.POST)
        print("in post")
        if form.is_valid():
            print('check')
            form.save()
            print("it is valid")
            use=User.objects.all()
            return render(request,'Home.html',{'user':use})
    else:
        form=forms.RegisterForm()
        print("in get")
        return render(request, 'Registration.html', {'form': form})