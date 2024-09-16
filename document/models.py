from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title