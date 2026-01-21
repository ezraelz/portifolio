from django.contrib import admin
from .models import Reaction

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'reaction', 'reacted_at'
    ]
