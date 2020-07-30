from django.contrib import admin
from .models import Article

# Register you
# r models here
class Admin_article(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_editable = ["name"]
    search_fields = ["name", "text"]

    class Meta:
        model = Article


admin.site.register(Article, Admin_article)


