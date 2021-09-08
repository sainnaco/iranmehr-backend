from django.contrib import admin

from blog.models import *
from .actions import make_published, make_draft
from accounts.models import UserAccount

User = UserAccount

# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ('get_main_category','sub_category')
# 	list_filter = (['main_category'])
# 	search_fields = ('main_category','sub_category')
	# prepopulated_fields = {'slug': ('title',)}

# class SubCategoryAdmin(admin.ModelAdmin):
# 	list_display = ('position', 'title','slug','status')
# 	list_filter = (['status'])
# 	search_fields = ('title', 'slug')
# 	prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
	# def formfield_for_foreignkey(self, db_field, request, **kwargs):
	# 	if db_field.name == "author":
	# 		kwargs["queryset"] = User.objects.filter(is_staff=True)
	# 	return super().formfield_for_foreignkey(db_field, request, **kwargs)


	list_display = ('title', 'thumbnail_tag','slug', 'author', 'jpublish', 'status') #, 'preview_url'
	list_filter = ('publish','status', 'author')
	search_fields = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-status', '-publish']
	actions = [make_published, make_draft]





admin.site.register(Article, ArticleAdmin)
# admin.site.register(Priority)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(IpAddress)
