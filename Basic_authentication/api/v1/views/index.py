#!/usr/bin/env python3
"""
Route module for the API
"""

from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

# New endpoint to raise 401 Unauthorized error
@app_views.route('/api/v1/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    abort(401)