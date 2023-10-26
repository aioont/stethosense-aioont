from django.db import models
from autho.models import LabUser, CustomUser


# Define choices for the lab_name field
LAB_REPORT_CHOICES = (
    ('Report 1', 'Report 1'),
    ('Report 2', 'Report 2'),
    ('Report 3', 'Report 3'),
    # Add more choices as needed
)

class LabReport(models.Model):
    lab = models.ForeignKey(LabUser, on_delete=models.CASCADE, related_name='lab_reports', null=True)
    name = models.CharField(max_length=100, choices=LAB_REPORT_CHOICES)
    description = models.TextField()
    date = models.DateField()
    results = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_reports', null=True)
    lab_report = models.FileField(upload_to='lab_reports/')

    # Additional fields for lab management
    lab_technician = models.CharField(max_length=100, null=True)  # Technician who conducted the lab test
    lab_location = models.CharField(max_length=100, null=True)  # Location or department of the lab
    lab_test_type = models.CharField(max_length=100, null=True)  # Type of lab test (e.g., blood test, urine test)
    lab_reference_range = models.CharField(max_length=100, null=True)  # Reference range for lab results
    is_urgent = models.BooleanField(default=False)  # Mark if the lab test is urgent
    is_confidential = models.BooleanField(default=False)  # Mark if the lab result is confidential

    def __str__(self):
        return self.name

