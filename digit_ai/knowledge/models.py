from django.db import models

# Create your models here.
# knowledge/models.py
class KnowledgeEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    created_by = models.ForeignKey('agents.Agent', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vector_embedding = models.JSONField(null=True, blank=True)
    tags = models.JSONField(default=list)
    
    def __str__(self):
        return self.title