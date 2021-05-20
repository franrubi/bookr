from django.contrib import admin

# Register your models here.
from reviews.models import Publisher, Contributor, \
    Book, BookContributor, Review
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')
    list_filter = ('publisher',)
    search_fields = ('title', 'isbn')

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)


