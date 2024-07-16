from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from Medassistapp.models import Blog
from Medassistapp.serializers import Blogserializer
from Medassistapp.serializers import BlogGetserializer


@api_view(['GET', 'POST', 'DELETE'])
def Submit_blog(request):
  
 try:
   if request.method=='POST':
    blog_serializer=Blogserializer(data=request.data)
    # print(doctor_serializer,doctor_serializer.is_valid(),request.data)
    if(blog_serializer.is_valid()):
    
      blog_serializer.save()
      return JsonResponse({"message":'blog data Submitted Successfully',"status":True},safe=False)
    else:
      return JsonResponse({"message":'Fail to  submit data',"status":False},safe=False) 
 except Exception as e:
    print("Error submit:",e)
    return JsonResponse({"message":'Fail to  submit data',"status":False},safe=False) 

@api_view(['GET', 'POST', 'DELETE'])
def BlogList(request):
 if request.method=='GET':
    bloglist=Blog.objects.all()
    blog_serializer = BlogGetserializer(bloglist,many=True)
    return JsonResponse(blog_serializer.data,safe=False)
 return JsonResponse({},safe=False) 