from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    #TODO: Need to be removed.
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
