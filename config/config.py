import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
FB_AUTH_TOKEN = os.getenv('FB_AUTH_TOKEN')
FB_VERIFY_TOKEN = os.getenv('FB_VERIFY_TOKEN')
FB_PAGE_ID = os.getenv('FB_PAGE_ID')

DB_DIR = 'data/db'
INPUT_FILE_PATH = 'data/input/sample.pdf'
OUTPUT_DIR = 'data/output'
