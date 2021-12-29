from django.contrib import admin

from .models import Group, Post, Follow, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'description',)
    search_fields = ('title',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'author', 'text',)
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):

    list_display = ('user', 'following',)
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Comment, CommentAdmin)
