# Code Editor - Setup and Run Guide

## Prerequisites
- Python 3.8+ installed
- Node.js 16+ and npm installed
- Docker installed (for code execution)

## Backend Setup

### 1. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the Backend Server
```bash
cd backend
uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`

#### Health Check
To verify the backend is running:
```
curl http://localhost:8000/health
```

## Frontend Setup

### 1. Install Frontend Dependencies
```bash
cd frontend/editor
npm install
```

### 2. Start the Development Server
```bash
cd frontend/editor
npm run dev
```

The frontend will typically be available at `http://localhost:5173` (or another port if 5173 is busy)

## Running the Application

### Step-by-step:

1. **Terminal 1 - Backend:**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```
   Wait for: `Uvicorn running on http://127.0.0.1:8000`

2. **Terminal 2 - Frontend:**
   ```bash
   cd frontend/editor
   npm run dev
   ```
   Wait for the local development server URL to appear

3. **Open Browser:**
   - Navigate to the frontend URL (typically `http://localhost:5173`)
   - Sign in with Firebase authentication
   - Use the code editor to write and execute code

## Features

✅ **Authentication:**
- Email/Password signup and login
- Google OAuth authentication
- Firebase integration

✅ **Code Editor:**
- Monaco Editor integration
- Python code execution
- Syntax highlighting
- Real-time code editing

✅ **Backend:**
- FastAPI server with CORS enabled
- Code execution endpoints
- Error handling
- Health check endpoint

## Troubleshooting

### "Cannot GET /" Error
- Make sure the frontend dev server is running on the correct port
- Check that `npm run dev` completed without errors

### "Failed to fetch" or Connection Error
- Ensure the backend is running: `uvicorn main:app --reload --port 8000`
- Check that port 8000 is not in use
- Verify CORS is enabled (it is in the updated main.py)

### Docker Issues (when running code)
- Ensure Docker daemon is running
- Check that Python, Java, C, C++ Docker images are built
- See docker/ folder for Dockerfile configuration

### Port Already in Use
- Backend (port 8000): `netstat -ano | findstr :8000` (Windows)
- Change port in code if needed and update frontend API calls

## File Structure

```
code_edit/
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── requirements.txt        # Python dependencies
│   ├── executor/
│   │   └── executor.py         # Code execution logic
│   ├── docker/                 # Docker files for code execution
│   └── app/
│       └── app.py              # Additional app logic
├── frontend/
│   └── editor/
│       ├── src/
│       │   ├── App.jsx         # Main app component
│       │   ├── Auth.jsx        # Authentication component
│       │   ├── firebase.js     # Firebase config
│       │   ├── components/
│       │   │   └── Editor.jsx  # Code editor component
│       │   └── ...
│       ├── package.json        # Node dependencies
│       └── vite.config.js      # Vite config
```

## Next Steps

1. Build and push Docker images for code execution
2. Set up environment variables for Firebase
3. Configure CORS for production if needed
4. Deploy to cloud platform (Azure, AWS, etc.)

