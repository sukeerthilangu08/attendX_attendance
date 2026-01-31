# attendX_attendance
# AttendX - Automated Attendance System

A web application for automated attendance using face recognition technology.

## 🚀 Features

- **Face Recognition**: Automatically detect and match faces in group photos
- **Student Database Integration**: Uses existing Student Images API (47 students)
- **Real-time Processing**: Upload group photo and get instant attendance results
- **Clean UI**: Simple, intuitive web interface
- **Detailed Results**: Shows present/absent students with statistics

## 🛠️ Tech Stack

**Frontend:**
- React.js 18
- Axios for API calls
- CSS3 for styling

**Backend:**
- Flask (Python)
- face_recognition library (dlib-based)
- OpenCV for image processing
- PIL for image handling

**Face Recognition:**
- face_recognition library with 128-dimensional face encodings
- Configurable tolerance for matching accuracy
- Multi-face detection in group photos

## 📁 Project Structure

```
attendX_attendance/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── face_matcher.py        # Face recognition logic
│   ├── student_api.py         # Student Images API client
│   ├── requirements.txt       # Python dependencies
│   └── uploads/              # Temporary upload folder
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AttendanceForm.js
│   │   │   └── ResultsDisplay.js
│   │   ├── App.js
│   │   └── App.css
│   └── package.json
└── SETUP_INSTRUCTIONS.md
```

## 🔧 Quick Start

1. **Clone and setup backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

2. **Setup frontend:**
```bash
cd frontend
npm install
npm start
```

3. **Test the system:**
```bash
python test_system.py
```

4. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## 📊 API Endpoints

### AttendX Backend API
- `POST /api/take-attendance` - Process group photo for attendance
- `GET /api/students` - Get all students from external API
- `GET /api/health` - Health check

### External Student Images API
- Base URL: http://192.168.13.183:5000
- `GET /api/images` - List all student images
- `GET /api/images/{id}` - Get specific image

## 🎯 How It Works

1. **Upload**: User uploads a group classroom photo
2. **Face Detection**: System detects all faces in the group photo
3. **Student Fetching**: Retrieves all 47 student images from external API
4. **Face Matching**: Compares each student's face with detected faces
5. **Results**: Returns present/absent students with statistics

## ⚡ Performance Optimization

- **Batch Processing**: Processes all students in a single request
- **Memory Management**: Cleans up uploaded files after processing
- **Configurable Tolerance**: Adjustable face matching sensitivity
- **Error Handling**: Robust error handling for API failures

## 🔒 Security Features

- File type validation (PNG, JPG, JPEG only)
- File size limits (16MB max)
- Secure filename handling
- CORS configuration for cross-origin requests

## 📝 Usage Tips

1. **Photo Quality**: Use high-resolution, well-lit group photos
2. **Face Visibility**: Ensure faces are clearly visible and not too small
3. **Naming Convention**: Student images should follow `Name_RollNumber.jpg` format
4. **Tolerance Tuning**: Adjust tolerance in `face_matcher.py` for accuracy

## 🐛 Troubleshooting

- **Face Recognition Issues**: Install cmake before face_recognition
- **API Connection**: Verify Student Images API is running
- **CORS Errors**: Ensure both frontend and backend are running
- **Memory Issues**: Reduce image size or adjust batch processing

## 📄 License

This is a student mini-project for educational purposes.