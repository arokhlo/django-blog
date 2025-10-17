from django.contrib import admin
from .models import Post  # Remove Comment if it doesn't exist

admin.site.register(Post)
# Remove this line if Comment doesn't exist: admin.site.register(Comment)