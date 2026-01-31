# Student Images API Documentation

## Base URL
```
http://192.168.13.183:5000
```

## Available Endpoints

### 1. Get All Images List
```
GET /api/images
```
Returns list of all images with metadata (id, filename, file_size, upload_date)

### 2. Get Specific Image
```
GET /api/images/{image_id}
```
Returns the actual image file (can be displayed directly in browser)

### 3. Get Image as Base64
```
GET /api/images/base64/{image_id}
```
Returns image as base64 encoded string with data URL

### 4. Search Images
```
GET /api/search?q={search_term}
```
Search images by filename

### 5. Get Statistics
```
GET /api/stats
```
Returns database statistics (total images, average size, total size)

## Example Usage

### Get all images:
```
curl http://192.168.13.183:5000/api/images
```

### View specific image (ID 1):
```
http://192.168.13.183:5000/api/images/1
```

### Search for images containing "Ayushi":
```
curl "http://192.168.13.183:5000/api/search?q=Ayushi"
```

### Get database stats:
```
curl http://192.168.13.183:5000/api/stats
```

## Total Images Available: 47
