from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .utils import get_random_code

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True
        

# Create your models here.
class SocialProfile(BaseModel):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="add your bio", max_length=300)
    email= models.EmailField()
    country = models.CharField(max_length=200)
    avatar=models.ImageField(default='avatar.png', upload_to='avatars/')
    friends=models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return f"{self.user.username}-{self.created_at.strftime('%d-%m-%Y')}"

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.get_friends().count()

    def get_post_num(self):
        return self.posts.all().count()

    def get_all_authors_posts(self):
        return self.posts.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value == 'Like':
                total_liked +=1
        return total_liked
    
    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0
        for post in posts:
            total_liked += post.num_of_likes()
        
        return total_liked

    def save(self, *args, **kwargs):
        code = get_random_code(self.email)
        if  self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name)+""+str(self.last_name))
            to_slug = slugify(str(to_slug)+ " " +code)
        else:
            to_slug = slugify(str(self.user)+" "+code)
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = [
    ('send', 'send'),
    ('accepted', 'accepted')
]
class Relationship(BaseModel):
    sender = models.ForeignKey(SocialProfile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(SocialProfile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
            
