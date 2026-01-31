#!/usr/bin/env python3
"""
Test script to verify AttendX system functionality
"""

import requests
import json

def test_student_api():
    """Test connection to Student Images API"""
    try:
        response = requests.get("http://192.168.13.183:5000/api/images")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Student API connected - {len(data)} students found")
            return True
        else:
            print(f"✗ Student API error: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Student API connection failed: {e}")
        return False

def test_backend_health():
    """Test AttendX backend health"""
    try:
        response = requests.get("http://localhost:8000/api/health")
        if response.status_code == 200:
            print("✓ AttendX backend is healthy")
            return True
        else:
            print(f"✗ Backend health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Backend connection failed: {e}")
        return False

def main():
    print("AttendX System Test")
    print("=" * 30)
    
    # Test external Student API
    student_api_ok = test_student_api()
    
    # Test our backend
    backend_ok = test_backend_health()
    
    print("\nTest Results:")
    print(f"Student Images API: {'✓ OK' if student_api_ok else '✗ FAIL'}")
    print(f"AttendX Backend: {'✓ OK' if backend_ok else '✗ FAIL'}")
    
    if student_api_ok and backend_ok:
        print("\n🎉 All systems ready! You can now use AttendX.")
    else:
        print("\n⚠️  Some services are not available. Check the setup instructions.")

if __name__ == "__main__":
    main()