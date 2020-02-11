from django.db import models

# Create your models here.

class BlogModel(models.Model):
    
    Title = models.CharField(max_length=450)

    Author = models.CharField(max_length=200)

    BlogBody = models.TextField()

    CreatedOn = models.DateTimeField('Date Published')

    ViewCount = models.IntegerField(default=0)

    PageLikes = models.IntegerField()

    BlogCategory = (
        ('Image', 'Image'),
        ('Video', 'Medium'),
        ('Default', 'Default'),
    )

    blog_cat = models.CharField(max_length=1, choices=BlogCategory)

    def _str_(self):
        return self.Title



class BlogComment(models.Model):
    blogs = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    Author = models.CharField()
    Comment = models.TextField()
    DatePosted = models.DateTimeField()


    def _str_(self):
        return self.Author