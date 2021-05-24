from django.core.checks import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from .forms import UploadImageForm,PostCommentForm,UpdateProfileForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def landing (request):
  post = Image.objects.all()
  form = PostCommentForm   
  comments =Comment.objects.all()

  title = 'Instagram'
  return render (request,'index.html',{'title':title,'Posts':post, 'comments':comments,"form": form})


@login_required(login_url='/accounts/login/')
def user_profile (request,userId):
  images = Image.objects.filter(creator=userId)
  print(images)
  profile=Profile.objects.all()
  return render(request, 'profile/profile.html', {'posts':images})



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


@login_required(login_url='/accounts/login/')
def comment_image(request,image_id):
  image = Image.objects.get(pk=image_id)
  comments = Comment.objects.filter(image=image)
  current_user =request.user
  if request.method == 'POST':
    form = PostCommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.user = current_user
      comment.image = Image.objects.get(pk=image_id)
      comment.save()
    return HttpResponseRedirect(reverse('comment_image', args=[image_id]))
  else:
    form = PostCommentForm   
  return render(request, 'comments/comment.html', {"image": image,"form": form,"comments": comments})




def search_results(request):
  if 'username' in request.GET and  request.GET["username"]:
    search_term = request.GET.get("username")
    searched_users = User.objects.filter(username__icontains=search_term)
    message =f"{search_term}"

    return render(request, 'search.html', {"message":message, "users":searched_users,})

  else:
    message = "You havent searched for any category"

    return render(request, 'search.html', {"message":message})


def edit_profile(request,userId):
  current_user =request.user
  if request.method == 'POST':
    form= UpdateProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile.email = current_user.email
      profile.save() 
      return HttpResponseRedirect(reverse('profile_page', args=[userId]))
  else:
    form = UpdateProfileForm
  return render (request, 'profile/edit_profile.html' , {"form": form})     






