from django.core.checks import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment

# Create your views here.

@login_required(login_url='/accounts/login/')
def landing (request):
  post = Image.objects.all()
  comments =Comment.objects.all()

  title = 'Instagram'
  return render (request,'profile/profile.html',{'title':title,'Posts':post, 'comments':comments})


def like (request, pk):
  image = get_object_or_404(Image, id=request.POST.get('image_id'))
  image.likes.add(request.user)
  return HttpResponseRedirect(reverse('landingPage'))



