import cv2
import numpy as np
from PIL import Image
from student_api import StudentAPIClient
from sklearn.metrics.pairwise import cosine_similarity

class FaceMatcher:
    def __init__(self):
        self.api_client = StudentAPIClient()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.similarity_threshold = 0.7
    
    def extract_student_name_roll(self, filename):
        """Extract name and roll number from filename"""
        try:
            name_part = filename.split('.')[0]
            if '_' in name_part:
                name, roll = name_part.rsplit('_', 1)
                return name.replace('_', ' '), roll
            else:
                return name_part.replace('_', ' '), "N/A"
        except:
            return filename, "N/A"
    
    def extract_face_features(self, image):
        """Extract face features using OpenCV"""
        if isinstance(image, Image.Image):
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        face_features = []
        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            # Resize to standard size and flatten as feature vector
            face_resized = cv2.resize(face_roi, (100, 100))
            face_features.append(face_resized.flatten())
        
        return face_features
    
    def process_group_photo(self, group_image_path):
        """Process group photo and match faces with student database"""
        # Load group photo
        group_image = cv2.imread(group_image_path)
        group_features = self.extract_face_features(group_image)
        
        print(f"Found {len(group_features)} faces in group photo")
        
        # Get all students from API
        students_data = self.api_client.get_all_students()
        print(f"Fetched {len(students_data)} students from API")
        
        present_students = []
        absent_students = []
        
        # Process each student
        for student in students_data:
            student_id = student['id']
            filename = student['filename']
            name, roll_number = self.extract_student_name_roll(filename)
            
            # Get student image
            student_image = self.api_client.get_student_image(student_id)
            if student_image is None:
                absent_students.append({
                    "name": name,
                    "roll_number": roll_number,
                    "image_id": student_id
                })
                continue
            
            # Extract features from student image
            student_features = self.extract_face_features(student_image)
            
            if len(student_features) == 0:
                print(f"No face found in student image: {filename}")
                absent_students.append({
                    "name": name,
                    "roll_number": roll_number,
                    "image_id": student_id
                })
                continue
            
            # Compare with group photo faces
            student_feature = student_features[0]
            is_present = False
            
            for group_feature in group_features:
                # Calculate similarity
                similarity = cosine_similarity(
                    [student_feature], [group_feature]
                )[0][0]
                
                if similarity > self.similarity_threshold:
                    is_present = True
                    break
            
            if is_present:
                present_students.append({
                    "name": name,
                    "roll_number": roll_number,
                    "image_id": student_id
                })
                print(f"✓ Found: {name} ({roll_number})")
            else:
                absent_students.append({
                    "name": name,
                    "roll_number": roll_number,
                    "image_id": student_id
                })
        
        return {
            "present_students": present_students,
            "absent_students": absent_students,
            "total_faces_detected": len(group_features),
            "total_students": len(students_data)
        }