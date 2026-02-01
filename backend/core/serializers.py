from rest_framework import serializers
from .models import (SMEProfile, Assessment, FundingSource, BusinessPlan,
                         FinancialProjection, UsageLog, Question, Answer)
from .validation import DataAnomalyDetector

class SMEProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMEProfile
        fields = '__all__'
        read_only_fields = ['user']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'response_value']

class AssessmentSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Assessment
        fields = '__all__'
        read_only_fields = ['user', 'score', 'ml_predicted_success', 'gap_analysis']

class FinancialProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProjection
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        detector = DataAnomalyDetector()
        request = self.context.get('request')
        sector = 'General'
        if request and request.user.is_authenticated:
            try:
                profile = request.user.smeprofile
                sector = profile.sector
            except SMEProfile.DoesNotExist:
                pass

        consistency_issues = detector.check_consistency({
            'revenue': data.get('revenue_year1'),
            'expenses': data.get('expenses_year1')
        })
        if consistency_issues:
            raise serializers.ValidationError(consistency_issues)

        return data

class BusinessPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPlan
        fields = '__all__'
        read_only_fields = ['user']

class FundingSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingSource
        fields = '__all__'

class UsageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageLog
        fields = '__all__'
