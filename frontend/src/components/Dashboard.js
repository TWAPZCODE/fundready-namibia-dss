import React from 'react';

const Dashboard = ({ userScore, mlPrediction, trustScore, explanation }) => {
  return (
    <div className="dashboard">
      <h1 className="text-2xl font-bold mb-6">SME Success Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="p-6 bg-white rounded-lg shadow">
          <h3 className="text-gray-500 text-sm uppercase">Readiness Score</h3>
          <p className="text-3xl font-bold text-blue-600">{userScore || 0}%</p>
          <p className="text-xs text-gray-400 mt-2">Based on expert-defined rules</p>
        </div>

        <div className="p-6 bg-white rounded-lg shadow">
          <h3 className="text-gray-500 text-sm uppercase">ML Success Probability</h3>
          <p className="text-3xl font-bold text-green-600">
            {mlPrediction ? (mlPrediction * 100).toFixed(1) : '0.0'}%
          </p>
          {explanation && (
            <div className="mt-2">
              <p className="text-xs text-green-700">✓ {explanation.top_positive?.[0]}</p>
              <p className="text-xs text-red-700">✗ {explanation.top_negative?.[0]}</p>
            </div>
          )}
        </div>

        <div className="p-6 bg-white rounded-lg shadow">
          <h3 className="text-gray-500 text-sm uppercase">Data Trust Score</h3>
          <p className="text-3xl font-bold text-purple-600">
            {trustScore ? (trustScore * 100).toFixed(0) : '50'}%
          </p>
          <div className="w-full bg-gray-200 h-2 rounded mt-2">
            <div
              className="bg-purple-600 h-2 rounded"
              style={{ width: `${(trustScore || 0.5) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      <div className="bg-blue-50 border-l-4 border-blue-400 p-4 mb-8">
        <div className="flex">
          <div className="ml-3">
            <p className="text-sm text-blue-700 font-bold">
              Predictive Insight:
            </p>
            <p className="text-sm text-blue-700">
              Your profile matches the "High Potential Growth" cluster for the Technology sector.
              Completing your "Marketing Strategy" could increase your probability by 12%.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
