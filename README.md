# Scanify AI

**An AI-Assisted Document Scanning, Image Processing, and Management Application**

Scanify AI is a web-based application designed to simplify document digitization and image processing. It enables users to upload documents, scan and enhance images, extract text through OCR, convert images into PDFs, and manage their documents through an intuitive interface.

The application combines a React-based frontend with a Python FastAPI backend, using OpenCV and other image-processing libraries for document processing.

## 1. Key Features

- **Document Upload:** Upload and preview document images.
- **Automatic Document Scanning:** Detect document boundaries and process images using OpenCV.
- **Manual Cropping:** Select and crop specific regions of an image.
- **Image Enhancement:** Apply filters to improve document appearance.
- **Image Resizing:** Adjust image dimensions.
- **Image Compression:** Reduce image file size.
- **Image Rotation:** Rotate images to the desired orientation.
- **PDF Conversion:** Convert images into PDF documents.
- **Optical Character Recognition (OCR):** Extract text from document images.
- **AI Integration:** Support AI-powered document-related functionality through an external API.
- **Authentication:** User authentication through Supabase.
- **Document Management:** Store and access documents using the configured storage services.

*Note: Some functionalities require external services, API credentials, or additional software configuration.*

## 2. Technology Stack

| Component | Technologies |
|---|---|
| Frontend | React 19, TypeScript, Vite |
| UI and Image Cropping | CSS, React Easy Crop |
| API Communication | Axios |
| Backend | Python, FastAPI, Uvicorn |
| Image Processing | OpenCV, NumPy, Pillow |
| OCR | Pytesseract, Tesseract OCR |
| Authentication and Storage | Supabase |
| AI Integration | OpenAI-compatible API |

## 3. Project Architecture

The application follows a frontend-backend architecture.

1. The **React frontend** provides the user interface for uploading, scanning, editing, and managing documents.
2. The **FastAPI backend** handles API requests and performs image-processing and document-related operations.
3. **OpenCV and Pillow** support image manipulation and document scanning.
4. **Pytesseract** provides OCR functionality for extracting text from images.
5. **Supabase** provides authentication and storage services.
6. An **external AI API** supports the configured AI-related functionality.

## 4. Repository Structure

```text
Section_C_Team_2/
│
├── Backend/
│   ├── main.py
│   ├── ai_utils.py
│   ├── image_utils.py
│   ├── ocr_utils.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── components/
│   │   ├── lib/
│   │   └── tools/
│   ├── package.json
│   └── package-lock.json
│
├── datasets/
│   └── README.md
│
├── implementation/
│   └── IMPLEMENTATION.md
│
├── docs/
│   ├── Scanify_AI_IPCV_Presentation_Polished.pptx
│   ├── Scanify_AI_IPCV_Report_Polished.docx
│   └── Scanify_AI_IPCV_Report_Polished.pdf
│
├── .gitignore
└── README.md
```

## 5. Prerequisites

Install the following before running the application:

- Python 3.11
- Node.js and npm
- Git
- Tesseract OCR (required for OCR functionality)
- Supabase project credentials
- AI API credentials (if using AI-powered functionality)

## 6. Clone the Repository

Open a terminal and execute:

```bash
git clone https://github.com/pragyatiwarii/Section_C_Team_2.git
cd Section_C_Team_2
```

## 7. Backend Setup

### Step 1: Navigate to the Backend Directory

```powershell
cd Backend
```

### Step 2: Create a Virtual Environment

```powershell
py -3.11 -m venv venv
```

### Step 3: Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file inside the `Backend` directory and add the environment variables required by the backend.

Configure the necessary AI API credentials and other service settings.

Do not upload actual API keys, passwords, or credentials to GitHub.

### Step 6: Start the Backend Server

```powershell
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The backend will be available at:

`http://127.0.0.1:8000`

Keep this terminal running.

## 8. Frontend Setup

Open a second terminal in the project root.

### Step 1: Navigate to the Frontend Directory

```powershell
cd frontend
```

### Step 2: Install Dependencies

```powershell
npm install
```

### Step 3: Configure Environment Variables

Create a `.env` file inside the `frontend` directory and provide the required Supabase configuration.

Use the variable names expected by the frontend configuration.

Never expose private service credentials in frontend environment variables.

### Step 4: Start the Development Server

```powershell
npm run dev
```

The terminal will display the frontend development URL. By default:

`http://localhost:5173`

Open this URL in your browser.

## 9. Environment and Security

The application uses environment variables to configure external services.

- Keep backend credentials in `Backend/.env`.
- Keep frontend configuration in `frontend/.env`.
- Do not commit API keys, passwords, or private credentials.
- Refer to the relevant service documentation for obtaining configuration values.

The repository's `.gitignore` excludes environment files and generated directories such as virtual environments and `node_modules`.

## 10. Testing Approach

The application was tested manually using sample document images.

Testing focused on the application's document upload, image scanning, cropping, image enhancement, image processing, and document conversion workflows.

No separate external or benchmark dataset was used. The application was evaluated using manually selected sample images rather than a dedicated training dataset.

Refer to `implementation/IMPLEMENTATION.md` and the final project report for further implementation and testing details.

## 11. Project Documentation

The following documents are included in the repository:

| Document | Location |
|---|---|
| Final Project Report (PDF) | `docs/Scanify_AI_IPCV_Report_Polished.pdf` |
| Editable Project Report | `docs/Scanify_AI_IPCV_Report_Polished.docx` |
| Project Presentation | `docs/Scanify_AI_IPCV_Presentation_Polished.pptx` |
| Implementation Details | `implementation/IMPLEMENTATION.md` |
| Dataset Information | `datasets/README.md` |

## 12. Future Enhancements

Potential improvements to Scanify AI include:

- Improving OCR accuracy and multilingual text recognition.
- Adding advanced PDF editing and processing capabilities.
- Implementing AI-powered document question answering.
- Generating summaries and questions from uploaded documents.
- Improving document organization, search, and retrieval.
- Enhancing scanning accuracy for complex document backgrounds.

## 13. Conclusion

Scanify AI aims to provide an integrated platform for document digitization and image processing. By combining computer vision, OCR, web technologies, and AI integration, the project demonstrates how multiple technologies can be brought together to simplify everyday document management tasks.