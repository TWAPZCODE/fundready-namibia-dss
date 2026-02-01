from django.db import models
from django.contrib.auth.models import User

class SMEProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100, blank=True)
    sector = models.CharField(max_length=100)
    years_in_operation = models.IntegerField(default=0)
    employee_count = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name

class DataTrustScore(models.Model):
    profile = models.OneToOneField(SMEProfile, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    last_calculated = models.DateTimeField(auto_now=True)
    verification_metrics = models.JSONField(default=dict)

class ValidationRule(models.Model):
    field_name = models.CharField(max_length=100)
    rule_type = models.CharField(max_length=50)
    parameters = models.JSONField()
    is_active = models.BooleanField(default=True)

class AnomalyAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_affected = models.CharField(max_length=100)
    anomaly_score = models.FloatField()
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class VerificationTask(models.Model):
    TASK_TYPES = [('DOCUMENT', 'Document Review'), ('FINANCIAL', 'Financial Audit')]
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='PENDING')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tasks')

class FundingSource(models.Model):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    description = models.TextField()
    amount_min = models.DecimalField(max_digits=12, decimal_places=2)
    amount_max = models.DecimalField(max_digits=12, decimal_places=2)
    funding_type = models.CharField(max_length=20)
    sector = models.CharField(max_length=100)
    requirements = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

class Question(models.Model):
    text = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    weight = models.IntegerField(default=1)

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    ml_predicted_success = models.FloatField(null=True, blank=True)
    gap_analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    assessment = models.ForeignKey(Assessment, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_value = models.IntegerField()

class BusinessPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    executive_summary = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

class FinancialProjection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    revenue_year1 = models.DecimalField(max_digits=12, decimal_places=2)
    expenses_year1 = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class UsageLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
