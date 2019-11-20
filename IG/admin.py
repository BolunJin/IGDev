from django.contrib import admin
from IG.models import Post, IGUser

# Register your models here.
# add apps which are displayed in admin page
admin.site.register(Post) # Regist model "Post" in app "admin"
admin.site.register(IGUser) # Regist model "IGUser" in app "admin"
