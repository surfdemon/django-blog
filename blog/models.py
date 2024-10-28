from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, "Published"))

# Create your models here.
class Post(models.Model):
    # Title field max length 200 charaters and unique 
    title = models.CharField(max_length=200, unique=True)
    # Slug field max length 200 charaters and unique 
    slug = models.SlugField(max_length=200, unique=True)
    # Author field is a forgeign key on User. on delete of author all their posts are deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    # Content text field 
    content = models.TextField()
    # Created on is date time field that is auto populated by time that the post entry is created
    created_on = models.DateTimeField(auto_now_add=True)
    # Status is default to 0 and can be 0 (draft) or 1 (published) based on the tuple that is assigned to the constant STATUS
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "author"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"



class Comment(models.Model):
    # Post forgiegn Key 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    # Author foreign Key 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    # comment text field 
    comment = models.TextField()
    # Approved bool 
    approved = models.BooleanField(default=False)
    # Created on date and time field that is auto populated with the current time and date
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.comment} by {self.author}"


