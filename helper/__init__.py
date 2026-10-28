from dotenv import load_dotenv, find_dotenv
import os
import sys

# define path base
base_path = os.path.abspath('..')
print('BASE_PATH =', base_path)
sys.path.append(base_path)


dotenv_path = find_dotenv('secret.env')
print(dotenv_path)


# execute .env file
load_dotenv(dotenv_path)

# load environment variables
db_user = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_connection_string = os.environ.get("CONECCTION_STRING")


# CONECCTION_STRING='mongodb+srv://{db_username}:{db_password}@aipy.duxgiko.mongodb.net/'
mongo_connection_string = db_connection_string.format_map(
    {
        'db_username': db_user,
        'db_password': db_password
    }
)