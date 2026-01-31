import React, { useState } from 'react';

const DocumentUpload = () => {
  const [isUploading, setIsUploading] = useState(false);
  const [decipherResult, setDecipherResult] = useState(null);

  const simulateProcessing = () => {
    setIsUploading(true);
    setTimeout(() => {
      setDecipherResult({
        detected_type: 'PDF Financial Statement',
        keywords: ['Revenue', 'Compliance', 'Operating Expenses', 'NamRA'],
        summary: 'AI detected a complete set of financial records for FY2023. Metrics appear consistent with SME profile.',
        confidence: 0.94
      });
      setIsUploading(false);
    }, 2500);
  };

  return (
    <div className="p-6 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">AI Document Decipherer</h2>
      <p className="text-gray-600 mb-4 text-sm">
        Upload any file (PDF, Image, Doc). Our integrated LLM will automatically extract
        key information to pre-fill your application.
      </p>

      <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center mb-6">
        <button
          onClick={simulateProcessing}
          disabled={isUploading}
          className="bg-blue-600 text-white px-6 py-2 rounded font-semibold hover:bg-blue-700 disabled:bg-gray-400"
        >
          {isUploading ? 'AI is analyzing your document...' : 'Upload Document'}
        </button>
      </div>

      {decipherResult && (
        <div className="bg-green-50 p-4 rounded-lg animate-fade-in">
          <h3 className="font-bold text-green-800 mb-2">Deciphering Complete</h3>
          <p className="text-sm text-green-700 mb-3">{decipherResult.summary}</p>
          <div className="flex flex-wrap gap-2">
            {decipherResult.keywords.map(word => (
              <span key={word} className="bg-green-200 text-green-800 text-xs px-2 py-1 rounded">
                {word}
              </span>
            ))}
          </div>
          <div className="mt-4 pt-4 border-t border-green-200">
            <p className="text-xs font-bold text-green-800">
              ✓ Trust Score increased by 15% due to verified document data.
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

export default DocumentUpload;
