from django.contrib import admin
from .models import * 


class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
	# prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('main_category','category_to_str')
	list_filter = (['main_category','sub_category'])
	search_fields = ('main_category', 'sub_category')
	filter_horizontal = ['sub_category']

	def category_to_str(self,obj):
		return ",".join([category.title for category in obj.sub_category.all()])
	category_to_str.short_description = 'دسته بندی فرعی'

admin.site.register(MainCategory)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Category,CategoryAdmin)
