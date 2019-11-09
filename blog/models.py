from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField() 
    depot_name = models.CharField(max_length=24)
class Blog_Model(models.Model):
    name = models.CharField(db_column='name', max_length=200, blank=True, verbose_name='name')

class Meta:
    db_table = 'Blog' # 定义了table的名字

