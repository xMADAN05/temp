fastapi-service/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── api/                       # API layer
│   │   ├── __init__.py
│   │   ├── deps.py                # Dependency injection
│   │   ├── routes.py              # API routes registration
│   │   └── v1/                    # API version 1
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── health.py      # Health check routes
│   │           └── items.py       # Resource endpoints
│   ├── core/                      # Core components
│   │   ├── __init__.py
│   │   ├── config.py              # Configuration management
│   │   ├── events.py              # Startup/shutdown events
│   │   ├── logging.py             # Logging configuration
│   │   └── security.py            # Authentication and security
│   ├── db/                        # Database access layer (for DynamoDB)
│   │   ├── __init__.py
│   │   └── dynamodb.py            # DynamoDB client/operations
│   ├── models/                    # Data models
│   │   ├── __init__.py
│   │   └── item.py                # Domain models
│   ├── schemas/                   # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── request.py             # Request schemas
│   │   └── response.py            # Response schemas
│   ├── services/                  # Business logic layer
│   │   ├── __init__.py
│   │   └── item_service.py        # Business logic
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       └── exceptions.py          # Custom exceptions
├── data/                          # Data storage (if needed)
│   └── .gitkeep
├── tests/                         # Tests
│   ├── __init__.py
│   ├── conftest.py                # Test configuration
│   ├── test_api/                  # API tests
│   │   └── test_endpoints/
│   │       ├── test_health.py
│   │       └── test_items.py
│   └── test_services/             # Service layer tests
│       └── test_item_service.py
├── Dockerfile                     # Docker configuration
├── .gitignore
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation