from django.contrib import admin

# Register your models here.
from app.models import *
from django.contrib import admin


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'owner')
    list_filter = ('owner',)
    search_fields = ('name',)