from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'text', 'pub_date')
    search_fields = ('author', 'title', 'text')
    list_filter = ('author', 'title', 'pub_date')
    empty_value_diplay = '-пусто-'


admin.site.register(Review, ReviewAdmin)
