from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.select_key = "your_secret_key"

