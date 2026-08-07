from include.extract import extract_data
from include.load_to_bucket import load_to_bucket
from include.load_to_snowflake import transfer_minio_data_to_snowflake
import time

api_response = extract_data()

load_to_bucket(api_response)

time.sleep(3)

transfer_minio_data_to_snowflake('triplens', 'raw/triplens_global.json', 'COUNTRIES_RAW')