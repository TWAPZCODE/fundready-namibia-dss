class DocumentDecipherer:
    """
    Interface for LLM-powered document analysis.
    Deciphers keywords and key financial metrics from uploaded files (PDF, Image, etc).
    """

    def decipher(self, file_obj):
        """
        Simulates LLM/OCR processing of an uploaded file.
        Returns extracted keywords and summary data.
        """
        file_name = file_obj.name.lower()

        # Simulated extraction results
        results = {
            'keywords': ['Revenue', 'Registration', 'Namibia', 'Compliance'],
            'detected_type': 'Unknown',
            'summary': 'Document processed successfully.',
            'extracted_metrics': {}
        }

        if file_name.endswith('.pdf'):
            results['detected_type'] = 'PDF Financial Statement'
            results['extracted_metrics'] = {'total_revenue': 450000, 'net_profit': 55000}
        elif file_name.endswith(('.jpg', '.jpeg', '.png')):
            results['detected_type'] = 'Scanned BIPA Certificate'
            results['keywords'].append('Registration Number')
            results['summary'] = 'Extracted BIPA registration details from image scan.'

        return results

    def verify_against_profile(self, extracted_data, profile):
        """
        Checks if the document matches the SME profile.
        """
        confidence_delta = 0.0
        if profile.company_name.lower() in extracted_data['summary'].lower():
            confidence_delta += 0.2

        return confidence_delta
