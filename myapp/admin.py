from django.contrib import admin
from .models import Post,Contact
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on','photo')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','message']
#admin.site.register(Post,  PostAdmin, Contact, ContactAdmin)


    


