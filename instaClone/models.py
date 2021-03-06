from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    user_name = models.CharField(max_length=30)
    profile_pic = CloudinaryField('image',null=True)
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def save_profile(self):
        self.save()

    def delete_username(self, user_name):
        self.objects.filter(user_name=user_name).delete()

    @classmethod
    def update_username(cls,user_name,new_name):
        update = Profile.objects.filter(user_name=user_name).update(user_name=new_name)
        return update

    @classmethod
    def update_bio(cls,user_name,bio):
        update = Profile.objects.filter(user_name=user_name).update(bio=bio)
        return update
        
    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['user_name']


class Image(models.Model):
  image= CloudinaryField('image',null=True)
  image_name = models.CharField(max_length=50)
  image_caption= models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  likes =models.ManyToManyField(User, related_name='likes',blank=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='creator')




  def likes_count(self):
      return self.likes.count()

  def save_image(self):
    return self.save()      

  def delete_image(self, image_name):
        return self.objects.filter(image_name=image_name).delete()   

  @classmethod
  def update_caption(cls,image_name,new_caption):
        update = Image.objects.filter(image_name=image_name).update(image_caption=new_caption)
        return update   


  def __str__(self):
        return self.image_name

  class Meta:
        ordering = ['-pub_date']       


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['pub_date']
    
