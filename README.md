# VeriVibe - News Facts Checker Backend

VeriVibe is a news fact-checking application that verifies news claims by cross-referencing with trusted sources.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
NEWS_API_KEY=your_news_api_key
FLASK_ENV=development
FLASK_APP=app
DATABASE_URL=sqlite:///verivibe.db
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the development server:
```bash
flask run
```

## Project Structure

```
verivibe/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── validators.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── fact_checker.py
│   │   ├── news_api.py
│   │   └── web_scraper.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_services.py
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── README.md
```

## API Endpoints

- `POST /api/v1/check`: Check a news claim
  - Input: Text or URL
  - Output: Fact-check results with sources

## Testing

Run tests using pytest:
```bash
pytest
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## License

MIT License 