from django.db import models
from django.core.validators import FileExtensionValidator
from social_profile.models import BaseModel, SocialProfile

# Create your models here.
class Post(BaseModel):
    author = models.ForeignKey(SocialProfile, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(
        upload_to='posts', 
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        blank=True
    )
    liked = models.ManyToManyField(SocialProfile, blank=True, related_name='likes')

    def __str__(self):
        return self.content[:20]
    

    def num_of_likes():
        return self.liked.all().count()

    def num_comments():
        return self.comment_set.all().count()
    
    # sort in newest to oldest post
    class Meta:
        ordering = ('-created_at',)


class Comment(BaseModel):
    user = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)

    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(BaseModel):
    user = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    
    
