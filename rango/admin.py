from django.contrib import admin
from rango.models import Category, Page 

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	fields = ["category", "title", "url", "views"]
	list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)

