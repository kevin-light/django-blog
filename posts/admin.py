from django.contrib import admin
from posts import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','update'] #控制admin展示哪些字段
    list_display_links = ['content']    #控制admin哪些展示字段的链接
    list_filter = ['update']            #支持在右侧过滤的字段
    search_fields = ['title']       #支持搜索的字段
    list_editable = ['title']     #支持直接编辑的字段，注意！不能与list_display_links重复！

    class Meta:
        model = models.Post

admin.site.register(models.Post,PostAdmin)