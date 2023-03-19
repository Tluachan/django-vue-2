from django.contrib import admin

from .models import Category, Product, Review

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('name','category','avg_rating')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, PageAdmin)
admin.site.register(Review)