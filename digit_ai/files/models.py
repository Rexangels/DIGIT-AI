from django.db import models

# Create your models here.
# files/models.py
class FileCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class UserFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='user_files/')
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(FileCategory, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class AgentFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='agent_files/')
    created_by = models.ForeignKey('agents.Agent', on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    category = models.ForeignKey(FileCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    analysis_results = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.name