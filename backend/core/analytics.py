import random

class PredictiveEngine:
    """
    Simulates ML models for SME funding success and gap clustering.
    In production, this would load trained models (e.g., joblib/pickle).
    """

    def predict_readiness_probability(self, profile_data, assessment_answers=None):
        # Simulated Predictive Model
        # Features: years_in_operation, employee_count, sector_encoded, etc.
        base_prob = 0.4
        years = profile_data.get('years_in_operation', 0)
        if years > 5:
            base_prob += 0.3
        elif years > 2:
            base_prob += 0.15

        if profile_data.get('registration_number'):
            base_prob += 0.2

        # Simulate model variance
        prediction = base_prob + random.uniform(-0.05, 0.05)
        return min(max(prediction, 0.0), 1.0)

    def identify_gap_clusters(self, sector):
        # Simulated Unsupervised Learning (K-Means)
        clusters = {
            'Agriculture': ['Collateral Shortfall', 'Seasonal Cash Flow Volatility'],
            'Mining': ['Environmental Compliance Gap', 'Equipment Financing Needs'],
            'Technology': ['Intellectual Property Strategy', 'Scalability Projections'],
            'General': ['Business Plan Clarity', 'Credit History Improvement']
        }
        return clusters.get(sector, clusters['General'])

    def get_shap_explanation(self, prediction):
        # Simulated Model Explainability (SHAP/LIME)
        if prediction > 0.7:
            return {
                'top_positive': ['Years in Operation', 'Formal Registration'],
                'top_negative': ['Low Employee Count']
            }
        else:
            return {
                'top_positive': ['Industry Sector Growth'],
                'top_negative': ['Inconsistent Financial Records', 'Short Operational History']
            }
