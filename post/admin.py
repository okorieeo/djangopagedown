from django.contrib import admin
from .models import Posts
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class PostsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    class Meta:
        model = Posts
admin.site.register(Posts, PostsAdmin)
