from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from posts import models
from . import forms
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def Index(request):
    queryset = models.Post.objects.all()
    # queryset = models.Post.objects.all().order_by('-timestamp')   #按时间倒序的两种方法

    paginator = Paginator(queryset, settings.PER_PAGE)  # m每页显示多少条数据

    page = request.GET.get('page')      #从请求中获取page参数，获取request请求的具体参数
    try:
        contacts = paginator.page(page)     #若果按照page能取到数据
    except PageNotAnInteger:
        # 取到page不是一个有效的数字
        contacts = paginator.page(1)    #返回第一页的内容
    except EmptyPage:
        # 但是page超出了有效的页码范围
        contacts = paginator.page(paginator.num_pages)  #返回最后一页的内容

    data = {'queryset':contacts}
    return render(request,'base.html',data)

    #redirect反向解析的3种方法：
    # return redirect('detail',id=3)  #detail url 定义的名字 post/3/
    # return redirect('post/3/')      #直接跳转到 post/3/
    # return redirect(reverse('detail',kwargs={"id":3}))

def detail(request,id=None):


    # obj = models.Post.objects.get(id=1)
    obj = get_object_or_404(models.Post,id=id)   #解决get内容不纯在报错
    # obj = get_object_or_404(models.Post,title__icontains='隔壁')   #解决get内容不纯在报错,title__icontains模糊查询
    data = {'obj':obj}
    return render(request,'detail.html',data)

def posts_create(request):

    # print(request.POST)   # 获取提交数据
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # instance = models.Post.create(title=title,content=content)
    # instance.save()
    form = forms.PostForm(request.POST or None)
    if form.is_valid():     #做数据库有效性验证
        instance = form.save()      #数据验证通过保存数据库
        messages.add_message(request,messages.INFO,'帖子创建成功')
    data = {'form':form}
    return render(request,'create.html',data)

def posts_update(request,id=None):
    """修改"""
    obj = get_object_or_404(models.Post, id=id)
    form = forms.PostForm(request.POST or None,instance=obj) #instance=obj instance关键字参数接收一个model实例，填充数据表格
    if form.is_valid():  # 做数据有效性验证
        instance = form.save()  # 存数据库
        # return redirect(instance.get_absolute_url())
        return redirect('/posts/%s/' %(id,))

    data = {
        "form": form
    }
    return render(request, "create.html", data)

def posts_delete(request,id=None):
    obj = get_object_or_404(models.Post,id=id)
    obj.delete()    #删除帖子
    return redirect('/posts/index/')












def Index_test01(request):

    return render(request,'home.html')


def Home_test01(request):

    return HttpResponse("HOme")