import React, { useState } from 'react';
import Dashboard from './components/Dashboard';
import DocumentUpload from './components/DocumentUpload';

function App() {
  const [view, setView] = useState('dashboard');

  return (
    <div className="App bg-gray-100 min-h-screen">
      <nav className="bg-white shadow-sm p-4 mb-6">
        <div className="max-w-7xl mx-auto flex gap-6 items-center">
          <span className="text-xl font-bold text-blue-800">FundReady Namibia</span>
          <div className="flex gap-4">
            <button
              onClick={() => setView('dashboard')}
              className={`px-3 py-2 rounded-md text-sm font-medium ${view === 'dashboard' ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'}`}
            >
              Dashboard
            </button>
            <button
              onClick={() => setView('upload')}
              className={`px-3 py-2 rounded-md text-sm font-medium ${view === 'upload' ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'}`}
            >
              AI Decipherer
            </button>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 pb-12">
        {view === 'dashboard' && (
          <Dashboard
            userScore={85}
            mlPrediction={0.88}
            trustScore={0.75}
            explanation={{
              top_positive: ['Formal BIPA Registration', '3 Years Financials'],
              top_negative: ['Small Team Size']
            }}
          />
        )}
        {view === 'upload' && <DocumentUpload />}
      </main>
    </div>
  );
}

export default App;
