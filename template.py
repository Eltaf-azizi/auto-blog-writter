import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



list_of_files = [
    ".github/workflows/.gitkeep",
    "backend/ingest_data.py",
    "backend/model.py",
    "static/style.css",
    "app.py",
    ".env",
    "Dockerfile",
    "requirements.txt",
    "templates/index.html",
    "test.py"
]