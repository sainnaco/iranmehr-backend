from django.contrib import admin
from .models import Pictures , Image ,Videos ,Clips

class PictureAdmin(admin.ModelAdmin):
	list_display = ('subject', 'thumbnail_tag','slug')
	search_fields = ('subject','slug')
	prepopulated_fields = {'slug': ('subject',)}
	filter_horizontal = ['images']
	# ordering = []
	# actions = []

class VideoAdmin(admin.ModelAdmin):
	list_display = ('subject', 'thumbnail_tag','slug')
	search_fields = ('subject','slug')
	prepopulated_fields = {'slug': ('subject',)}
	filter_horizontal = ['clip']
	# ordering = []
	# actions = []

admin.site.register(Pictures,PictureAdmin)
admin.site.register(Image)
admin.site.register(Videos,VideoAdmin)
admin.site.register(Clips)