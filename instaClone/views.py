from django.core.checks import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from .forms import UploadImageForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def landing (request):
  post = Image.objects.all()
  comments =Comment.objects.all()

  title = 'Instagram'
  return render (request,'index.html',{'title':title,'Posts':post, 'comments':comments})


@login_required(login_url='/accounts/login/')
def user_profile (request,username):
  user_profile = get_object_or_404(User, username=username)
  posts = user_profile.image.all()

  print(posts)


  profile=Profile.objects.all()


  return render(request, 'profile/profile.html', {'posts':posts})



@login_required(login_url='/accounts/login/')
def like (request, pk):
  image = get_object_or_404(Image, id=request.POST.get('image_id'))
  image.likes.add(request.user)
  return HttpResponseRedirect(reverse('landingPage'))


@login_required(login_url='/accounts/login/')
def upload_image(request):
  current_user =request.user
  if request.method == 'POST':
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.save(commit=False)
      image.creator = current_user
      image.save()
    return redirect(landing)
  else:
    form = UploadImageForm
  return render(request, 'upload.html', {"form": form})    



