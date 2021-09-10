from django.contrib import admin

from blog.models import *
from .actions import make_published, make_draft
from accounts.models import UserAccount

User = UserAccount


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'thumbnail_tag','slug', 'author', 'jpublish', 'status') #, 'preview_url'
	list_filter = ('publish','status', 'author')
	search_fields = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-status', '-publish']
	actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment, CommentAdmin)

