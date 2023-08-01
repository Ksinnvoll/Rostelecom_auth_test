import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')
phone = os.getenv('phone')
temp_email = os.getenv('temp_email')
