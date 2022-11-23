from django.contrib import admin

from main.models import Product, ProductFile


class InlineProductFile(admin.TabularInline):
    model = ProductFile
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductFile]
    list_display = ('id', 'name', 'vendor_code', 'creator_user')
    list_display_links = ('id', 'name', 'vendor_code', 'creator_user')
    fields = (
    'id', 'creator_user', 'vendor_code', 'name', 'description', 'created',
    'updated',)
    readonly_fields = ('id', 'created', 'updated',)


admin.site.register(Product, ProductAdmin)
