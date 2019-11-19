from django.contrib import admin
from IG.models import Post

# Register your models here.
# add apps which are displayed in admin page
admin.site.register(Post) # Regist model "Post" in app "admin"