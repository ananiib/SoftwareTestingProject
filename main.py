import logging
from behave.__main__ import main as behave_main

try:
    behave_main("features")
except Exception as e:
    logging.error(f"Test execution failed: {e}")
