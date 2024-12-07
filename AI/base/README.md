```bash
project-root/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py           # API route definitions
│   │   └── dependencies.py     # Shared dependencies for the API
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py           # Configuration settings (e.g., environment variables)
│   ├── models/
│   │   ├── __init__.py
│   │   └── response_model.py   # Response models or schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini_service.py   # Logic to interact with Gemini API
│   │   └── parsing_service.py  # Parsing or processing logic
│   ├── utils/
│   │   ├── __init__.py
│   │   └── file_utils.py       # File handling utilities
│   └── main.py                 # Entry point for FastAPI application
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # Unit tests for routes
│   └── test_services.py        # Unit tests for services
├── prompt.txt
├── README.md
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── .gitignore
```