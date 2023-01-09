from django.contrib import admin
from posts.models import Post, Cathegory

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, AuthorAdmin)
admin.site.register(Cathegory, AuthorAdmin)