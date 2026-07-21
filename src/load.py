import os
import logging
from dotenv import load_dotenv
from urllib.parse import quote_plus

from transform import transform_data
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

db_user = os.getenv("DB_USER")
db_password = quote_plus(os.getenv("DB_PASSWORD"))
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

try:

    file_path = "data/netflix_titles.csv"
    df = transform_data(file_path)


    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    with engine.begin() as connection:
        logging.info("Connected to PostgreSQL successfully.")

        connection.execute(text("TRUNCATE TABLE movies"))
        logging.info("Movies table cleared.")


        df.to_sql(
            name="movies",
            con=connection,
            if_exists="append",
            index=False
        )

        logging.info("Data loaded successfully.")

except Exception as e:
    logging.error(f"ETL pipeline failed: {e}")
    print(f"Error: {e}")
