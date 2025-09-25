#!/usr/bin/env python3
"""
DrugTox-AI Dashboard - Backend Entry Point
==========================================

Main entry point for the Flask backend application.
"""

import os
import sys
from app import app, predictor

if __name__ == '__main__':
    # Get the port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))

    # Show startup banner
    print("🧬 DrugTox-AI Enhanced Dashboard")
    print("=" * 40)
    print(f"📊 Dashboard: http://localhost:{port}")
    print(f"🔬 Prediction API: http://localhost:{port}/api/predict")
    print(f"📈 Statistics: http://localhost:{port}/api/stats")
    print(f"🎯 Endpoints loaded: {len(predictor.endpoints)}")
    print(f"🤖 Model status: {'Active' if predictor.is_loaded else 'Mock Mode'}")
    print("=" * 40)

    # Run the Flask application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    )