from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Profile,Comment

# Create your views here.

def landing (request):
  post = Image.objects.all()
  comments =Comment.objects.all()


  title = 'Instagram'
  return render (request,'index.html',{'title':title,'Posts':post, 'comments':comments})