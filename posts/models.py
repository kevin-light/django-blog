from django.db import models
from django.urls import reverse
# Create your models here.

# MVC model,view,controllers
# MVT model,view,Template

class Post(models.Model):

    title = models.CharField(max_length=128)  #标题
    content = models.TextField()    #内容
    timestamp = models.DateTimeField(auto_now=True)     #发表时间
    update = models.DateTimeField(auto_now_add=True)    #跟新时间

    def __str__(self):
        return self.title       #后台管理显示的入口信息

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id':self.id})
        # return "/posts/%s/" % (self.id)
        # return "/posts/{}/".format(self.id)

