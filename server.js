// Minimal Express server: serves API and static client build
const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Example API route
app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from FundReady Namibia DSS API' });
});

// Serve static files from client build
const buildPath = path.join(__dirname, 'client', 'build');
app.use(express.static(buildPath));
app.get('*', (req, res) => {
  res.sendFile(path.join(buildPath, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});