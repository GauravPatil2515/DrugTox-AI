# 🧬 DrugTox-AI Dashboard

A comprehensive web-based platform for molecular toxicity prediction using machine learning models.

## 📁 Project Structure

```text
drugtox-dashboard/
├── backend/                    # Flask API Backend
│   ├── app/
│   │   ├── __init__.py        # Main Flask application
│   │   ├── models/            # ML model integration
│   │   ├── routes/            # API endpoints
│   │   ├── services/          # Business logic
│   │   └── utils/             # Utility functions
│   ├── requirements.txt       # Python dependencies
│   ├── tests/                 # Backend tests
│   └── migrations/            # Database migrations (future)
├── frontend/                  # Frontend Assets
│   ├── src/
│   │   ├── assets/            # CSS, JS, Images
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page templates
│   │   └── utils/             # Frontend utilities
│   ├── public/                # Static files
│   └── dist/                  # Build output (future)
├── docs/                      # Documentation
├── scripts/                   # Deployment scripts
├── tests/                     # Integration tests
├── README.md                  # This file
└── requirements.txt           # Project dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Git

### Installation

1. **Clone and setup:**

   ```bash
   git clone <repository-url>
   cd drugtox-dashboard
   ```

2. **Backend setup:**

   ```bash
   cd backend
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python -m app
   ```

4. **Access dashboard:**
   Open [http://localhost:5000](http://localhost:5000)

## 🔧 Development

### Backend Development

```bash
cd backend
# Install in development mode
pip install -e .
# Run with auto-reload
FLASK_ENV=development flask run
```

### Frontend Development

```bash
cd frontend
# Install dependencies (future)
npm install
# Start development server (future)
npm run dev
```

## 📊 Features

- **Molecular Toxicity Prediction** - 12 toxicity endpoints
- **Batch Processing** - Handle multiple molecules
- **Interactive Dashboard** - Modern web interface
- **REST API** - Programmatic access
- **Result Management** - History and export
- **Responsive Design** - Mobile-friendly

## 🔗 API Documentation

See [API Documentation](./docs/api.md) for detailed endpoint information.

## 🧪 Testing

```bash
# Backend tests
cd backend
python -m pytest

# Integration tests
cd tests
python -m pytest
```

## 🚀 Deployment

See [Deployment Guide](./docs/deployment.md) for production deployment instructions.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📞 Support

For questions and support, please open an issue on GitHub.

---

Built with ❤️ for safer drug discovery
