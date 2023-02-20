import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
TEST_DB_USER = os.environ.get("TEST_DB_USER", "test")
TEST_DB_PASS = os.environ.get("TEST_DB_PASS", "test")
TEST_DB_HOST = os.environ.get("TEST_DB_HOST", "localhost")
TEST_DB_PORT = os.environ.get("TEST_DB_PORT", 5432)
TEST_DB_NAME = os.environ.get("TEST_DB_NAME", "test")
