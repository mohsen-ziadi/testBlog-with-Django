from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    STATUS_CHOICE=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish= models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='published')

    class Meta:
        ordering=('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post-detail',args=[self.slug,self.id])
    def __str__(self):
        return self.title

class Account(models.Model):
    GENDER_CHOICE=(
        ('male','male'),
        ('female','female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='account')
    gender = models.CharField(max_length=7,choices=GENDER_CHOICE,default='male')
    phone = models.CharField(max_length=11,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

