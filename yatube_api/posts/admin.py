from django.contrib import admin
from .models import Post, Group, Comment


class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author',)
    list_filter = ('pub_date',)
    search_fields = ('text',)
    empty_value_display = '-Пусто-'


admin.site.register(Post, AdminPost)
admin.site.register(Group)
admin.site.register(Comment)
