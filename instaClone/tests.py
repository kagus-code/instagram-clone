from django.http import request
from django.test import TestCase
from .models import Profile,Image,Comment
from django.contrib.auth.models import User




class ImageTestClass(TestCase):
   def setUp(self):
     self.image = Image(image='cloudinaryfield',image_name='machu pichu',image_caption='amazing stuff',pub_date=2012-20-14)

   def test_instance(self):
     self.assertTrue(isinstance(self.image,Image))  

   def test_save_method(self):
     self.image.save_image()
     images = Image.objects.all()  
     self.assertTrue(len(images) > 0)  

   
   def test_delete_method(self):
        self.image.save_image()
        Image.delete_image(Image, image_name='machu pichu')
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)   

    
   def test_update_location(self):
        self.image.save_image()
        Image.update_caption(image_name='machu pichu', new_caption='great ruins')
        self.assertTrue(Image.objects.get(image_caption='great ruins')) 

   
   def tearDown(self):
        Image.objects.all().delete()          

class CommentTestClass(TestCase):

    def setUp(self):
        self.comment = Comment(
            comment='nature', )

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.comment, Comment))


    def tearDown(self):
        Comment.objects.all().delete()  

class ProfileTestClass(TestCase):
  def setUp(self):
     self.profile= Profile(user_name='king',profile_pic='clodinaryfield',bio='something personal',email='ekagus@gmail.com')
  
  def test_instance(self):
       self.assertTrue(isinstance(self.profile, Profile))

  def test_save_profile(self):
    self.profile.save_profile()
    profiles=Profile.objects.all()
    self.assertTrue(len(profiles) > 0)

  def test_delete_username(self):
    self.profile.save_profile()
    Profile.delete_username(Profile,user_name='king')
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) == 0)  

  def test_update_profile(self):
    self.profile.save_profile()
    Profile.update_bio(user_name='king',bio='new-bio')
    self.assertTrue(Profile.objects.get(bio='new-bio'))





  def tearDown(self):
        Profile.objects.all().delete()       



# Create your tests here.
