<h1 align="center">✍️ auto-blog-writter</h1>

**auto-blog-writter** is a simple and efficient AI-powered application that automatically generates blog posts based on a given topic. It provides an API interface and uses advanced language models to create high-quality content with minimal input.


## 📌 Features

- Generate complete blog posts using AI
- REST API for seamless integration
- Easy to configure and run locally or in Docker
- Modular structure for better maintainability


## Project Structure

    .github/workflows/
    .gitkeep
    backend/
    ├── __pycache__/
    ├── generate_blog.py
    .env
    app.py
    Dockerfile
    endpoint.py
    README.md
    requirements.txt
    template.py


## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/auto-blog-writter.git
cd auto-blog-writter
```

### 2. Create a Virtual Environment
```bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```

### 4. Add Your Environment Variables
Create a .env file in the root directory:

```ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the App
```bash
Copy
Edit
python app.py
```

## 🐳 Run with Docker (Optional)
#### Build the Image
```bash
Copy
Edit
docker build -t auto-blog-writter .
```
#### Run the Container
```bash
Copy
Edit
docker run -p 5000:5000 auto-blog-writter
```


