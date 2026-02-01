from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SMEProfileViewSet, AssessmentViewSet, BusinessPlanViewSet,
                    FinancialProjectionViewSet, FundingSourceViewSet, UsageLogViewSet,
                    QuestionViewSet)

router = DefaultRouter()
router.register(r'profiles', SMEProfileViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'business-plans', BusinessPlanViewSet)
router.register(r'financial-projections', FinancialProjectionViewSet)
router.register(r'funding-sources', FundingSourceViewSet)
router.register(r'usage-logs', UsageLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
