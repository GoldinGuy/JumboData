web: gunicorn api_server:app --log-file -
release: python3 init_db.py
worker: python3 start_api.py
processor: python3 start_scraper.py