from flask import Flask, render_template_string
from config import *
from routes import register_routes
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Register all routes
register_routes(app)

if __name__ == '__main__':
    # Auto-reload enabled
    # app.run(ssl_context='adhoc', debug=True, host='0.0.0.0', port=5000, use_reloader=True)
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)
