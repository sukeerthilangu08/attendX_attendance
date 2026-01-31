#!/bin/bash

echo "🚀 Starting AttendX System..."

# Start backend in background
echo "📡 Starting backend server on port 5001..."
cd backend
python3 app.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
echo "🌐 Starting frontend server on port 3000..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo "✅ System started!"
echo "Backend: http://localhost:5001"
echo "Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for user to stop
wait