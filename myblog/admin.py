from django.contrib import admin
from .models import post

# Register your models here.
#ths class helps us to change the view of how our admin pane will look like
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','created_on','status')
    list_filter=('status',)
    search_fields=('title','content')#adds a search criteria to our site
    prepopulated_fields={'slug':('title',)}
admin.site.register(post,PostAdmin)
