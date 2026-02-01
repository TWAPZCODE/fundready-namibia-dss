from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (SMEProfile, Assessment, FundingSource, BusinessPlan,
                         FinancialProjection, UsageLog, VerificationTask, Question)
from .serializers import (SMEProfileSerializer, AssessmentSerializer, FundingSourceSerializer,
                         BusinessPlanSerializer, FinancialProjectionSerializer, UsageLogSerializer,
                         QuestionSerializer)
from .analytics import PredictiveEngine

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

class SMEProfileViewSet(viewsets.ModelViewSet):
    queryset = SMEProfile.objects.all()
    serializer_class = SMEProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        UsageLog.objects.create(
            user=self.request.user,
            action="Created SME Profile",
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT')
        )

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        profile = None
        try:
            profile = user.smeprofile
        except SMEProfile.DoesNotExist:
            pass

        engine = PredictiveEngine()
        profile_data = {
            'years_in_operation': profile.years_in_operation if profile else 0,
            'registration_number': profile.registration_number if profile else ''
        }
        prediction = engine.predict_readiness_probability(profile_data)

        serializer.save(
            user=user,
            score=int(prediction * 100),
            ml_predicted_success=prediction,
            gap_analysis=", ".join(engine.identify_gap_clusters(profile.sector if profile else 'General'))
        )
        UsageLog.objects.create(user=user, action="Completed Assessment")

    @action(detail=False, methods=['get'])
    def predictions(self, request):
        user = request.user
        profile = getattr(user, 'smeprofile', None)
        engine = PredictiveEngine()
        prediction = engine.predict_readiness_probability({
            'years_in_operation': profile.years_in_operation if profile else 0,
            'registration_number': profile.registration_number if profile else ''
        })
        explanation = engine.get_shap_explanation(prediction)
        return Response({
            'ml_predicted_success': prediction,
            'explanation': explanation
        })

class BusinessPlanViewSet(viewsets.ModelViewSet):
    queryset = BusinessPlan.objects.all()
    serializer_class = BusinessPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        UsageLog.objects.create(user=self.request.user, action="Updated Business Plan")

class FinancialProjectionViewSet(viewsets.ModelViewSet):
    queryset = FinancialProjection.objects.all()
    serializer_class = FinancialProjectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        UsageLog.objects.create(user=self.request.user, action="Updated Financial Projections")

class FundingSourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundingSource.objects.all()
    serializer_class = FundingSourceSerializer
    permission_classes = [permissions.AllowAny]

class UsageLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UsageLog.objects.all()
    serializer_class = UsageLogSerializer
    permission_classes = [permissions.IsAdminUser]
