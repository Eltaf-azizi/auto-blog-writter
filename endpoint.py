import os
from flask import Flask, request, jsonify
from backend.generate_blog import generate_blog


app = Flask(__name__)


@app.route('/generate_blog', methods=['POST'])

def generate_blog_endpoint():
    """
    Handles blog generation requests.
    """
    data = request.json
    topic = data.get("topic", "")
