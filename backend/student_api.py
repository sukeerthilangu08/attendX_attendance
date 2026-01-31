import requests
import base64
from io import BytesIO
from PIL import Image
import numpy as np

class StudentAPIClient:
    def __init__(self, base_url="http://192.168.13.183:5000"):
        self.base_url = base_url
    
    def get_all_students(self):
        """Fetch all student images metadata"""
        try:
            response = requests.get(f"{self.base_url}/api/images")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching students: {e}")
            return []
    
    def get_student_image(self, image_id):
        """Fetch student image as PIL Image"""
        try:
            response = requests.get(f"{self.base_url}/api/images/{image_id}")
            response.raise_for_status()
            return Image.open(BytesIO(response.content))
        except requests.RequestException as e:
            print(f"Error fetching image {image_id}: {e}")
            return None
    
    def get_student_image_base64(self, image_id):
        """Fetch student image as base64"""
        try:
            response = requests.get(f"{self.base_url}/api/images/base64/{image_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching base64 image {image_id}: {e}")
            return None