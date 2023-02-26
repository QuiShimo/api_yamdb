from django.contrib import admin

from reviews.models import Comments, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'text', 'pub_date')
    search_fields = ('author', 'title', 'text')
    list_filter = ('author', 'title', 'pub_date')
    empty_value_diplay = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'review', 'text', 'pub_date')
    search_fields = ('author', 'review')
    list_filter = ('author', 'review', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comments, CommentAdmin)
