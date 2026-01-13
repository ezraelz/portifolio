from django.db import models

class PageView(models.Model):
    page = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

