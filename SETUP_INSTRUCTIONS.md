# AttendX Setup and Run Instructions

## Prerequisites
- Python 3.8+
- Node.js 16+
- Student Images API running at http://192.168.13.183:5000

## Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
python app.py
```
Backend will run on http://localhost:5001

## Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```
Frontend will run on http://localhost:3000

## Usage

1. Open http://localhost:3000 in your browser
2. Upload a group classroom photo
3. Click "Take Attendance"
4. View the results showing present/absent students

## API Endpoints

### Backend API (http://localhost:5001)
- `GET /api/health` - Health check
- `POST /api/take-attendance` - Process attendance (multipart/form-data with 'image' field)
- `GET /api/students` - Get all students from external API

## Performance Tips

1. **Image Quality**: Use high-resolution group photos for better face detection
2. **Lighting**: Ensure good lighting conditions in the photo
3. **Face Size**: Faces should be clearly visible (not too small or blurred)
4. **Tolerance Adjustment**: Modify `tolerance` in `face_matcher.py` (0.4-0.8 range)
   - Lower = stricter matching
   - Higher = more lenient matching

## Troubleshooting

1. **Face Recognition Installation Issues**:
   ```bash
   # On macOS
   brew install cmake
   
   # On Ubuntu
   sudo apt-get install cmake
   ```

2. **CORS Issues**: Make sure both servers are running and frontend proxy is configured

3. **Student API Connection**: Verify the Student Images API is accessible at http://192.168.13.183:5000

## File Naming Convention

Student images should follow the format: `Name_RollNumber.jpg`
Example: `John_Doe_12345.jpg`