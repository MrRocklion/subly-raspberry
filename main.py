from Subly import SublyBackend
from dotenv import load_dotenv
import os
from logger_config import logger

load_dotenv(dotenv_path=".env", override=True)
api_url = os.getenv("API_URL")
tenant = os.getenv("TENANT_ID")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")




backend = SublyBackend(tenant, api_url, username, password)
users = backend.get_users()
for user in users:
    print(user)

