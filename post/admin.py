from django.contrib import admin

from post.models import (
    Post,
    Favorite,
    Category,
    Socials,
    UserProfile,
    )
from comment.models import Comment


# @admin.register(Category)
# class CategoryInline(admin.TabularInline):
#     model = Category
#     extra = 2


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = [
#         'author',
#         'title',
#         'created_date',
#         'updated_on',
#         'date_published',
#         'publish',
#         'views',
#     ]
# inlines = [CategoryInline]


admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Favorite)
admin.site.register(Socials)
admin.site.register(Post)
admin.site.register(Category)
