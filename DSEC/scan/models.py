from django.db import models

class Scan(models.Model):
    project_name = models.CharField(max_length=255)
    scan_name = models.CharField(max_length=255)
    scan_id = models.CharField(max_length=100, unique=True)
    tools_name = models.CharField(max_length=255)
    scan_author = models.CharField(max_length=255)
    scan_config_file_path = models.TextField()
    result_file_path = models.TextField()
    scan_status = models.CharField(max_length=50)
    trash = models.BooleanField(default=False)
    

    def __str__(self):
        return self.project_name
