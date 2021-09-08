from django.contrib import admin
from .models import * 


class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
	# prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	list_filter = (['main_category','sub_category'])
	search_fields = ('main_category', 'sub_category')
	filter_horizontal = ['sub_category']

admin.site.register(MainCategory)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Category,CategoryAdmin)
