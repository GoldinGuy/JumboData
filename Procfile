web: gunicorn api_server:app --log-file -
worker: python3 start_api.py
processor: python3 start_scraper.py