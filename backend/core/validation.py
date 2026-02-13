import numpy as np

class DataAnomalyDetector:
    def __init__(self, sector_data=None):
        self.sector_data = sector_data or {}

    def detect_outlier(self, field_name, value, sector):
        # Placeholder for sector-based Z-score detection
        # In a real app, this would query historical data for the sector
        benchmarks = {
            'Agriculture': {'revenue': 500000, 'std': 200000},
            'Mining': {'revenue': 5000000, 'std': 1000000},
        }

        if sector in benchmarks and field_name in benchmarks[sector]:
            stats = benchmarks[sector]
            mean = stats[field_name]
            std = stats['std']
            z_score = abs((float(value) - mean) / std)
            return z_score > 3 # Flag if > 3 standard deviations
        return False

    def check_consistency(self, data):
        issues = []
        revenue = float(data.get('revenue', 0))
        expenses = float(data.get('expenses', 0))

        if revenue < 0:
            issues.append("Revenue cannot be negative.")
        if revenue > 0 and expenses > revenue * 10:
            issues.append("Expenses are unusually high relative to revenue (over 10x).")

        return issues

def calculate_trust_score(data, verification_status):
    """
    Calculates a trust score from 0.0 to 1.0
    """
    base_score = 0.5
    if verification_status.get('documents_verified'):
        base_score += 0.3
    if verification_status.get('consistent_history'):
        base_score += 0.2
    return min(base_score, 1.0)
