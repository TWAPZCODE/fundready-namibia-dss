from django.core.management.base import BaseCommand
from core.models import Question, FundingSource

class Command(BaseCommand):
    help = 'Seed the database with initial Namibian funding sources and questions'

    def handle(self, *args, **kwargs):
        # Questions
        questions = [
            ("Is your business registered with BIPA?", "Registration", 10),
            ("Do you have a formal business plan?", "Planning", 8),
            ("Do you keep separate bank accounts for business and personal use?", "Financials", 7),
        ]
        for text, cat, weight in questions:
            Question.objects.get_or_create(text=text, category=cat, weight=weight)

        # Funding Sources
        sources = [
            {
                "name": "SME Special Loan",
                "organization": "FNB Namibia",
                "description": "Tailored loan for growing SMEs.",
                "amount_min": 50000,
                "amount_max": 1000000,
                "funding_type": "Loan",
                "sector": "General",
                "requirements": "BIPA Registration, 12 months bank statements."
            },
            {
                "name": "Agri-Business Grant",
                "organization": "DBN",
                "description": "Support for innovative agriculture.",
                "amount_min": 100000,
                "amount_max": 5000000,
                "funding_type": "Grant",
                "sector": "Agriculture",
                "requirements": "Project proposal, land ownership proof."
            }
        ]
        for s in sources:
            FundingSource.objects.get_or_create(**s)

        self.stdout.write(self.style.SUCCESS('Successfully seeded Namibia DSS Database'))
