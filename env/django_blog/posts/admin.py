from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    '''Admin Model for Post model'''
    list_display = ["timestamp", "updated", "title", "content"]
    list_display_links = ["updated"]
    list_filter = ['updated', "timestamp"]
    search_fields = ['title', 'content']
    list_editable = ["title", 'content']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)


