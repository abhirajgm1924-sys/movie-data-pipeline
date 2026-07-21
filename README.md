# 🎬 Movie Data Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline built with **Python**, **Pandas**, and **PostgreSQL**. The project extracts movie data from a CSV file, cleans and transforms it, and loads it into a PostgreSQL database using SQLAlchemy.

This project was built to demonstrate practical data engineering skills, including database integration, environment variable management, logging, and transaction handling.

---

## 🚀 Features

- Extract movie data from a CSV file using Pandas
- Clean and transform raw data
- Remove duplicate records
- Handle missing values
- Select only relevant columns
- Load cleaned data into PostgreSQL
- Secure database credentials using `.env`
- Logging with timestamps and log levels
- Transaction-based database operations
- Idempotent ETL pipeline (safe to run multiple times)

---

## 🛠️ Tech Stack

- Python 3
- Pandas
- PostgreSQL
- SQLAlchemy
- psycopg2
- python-dotenv
- Logging

---

## 📂 Project Structure

```
movie-data-pipeline/
│
├── data/
│   └── netflix_titles.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ ETL Workflow

### 1. Extract

- Read the Netflix dataset from a CSV file using Pandas.

### 2. Transform

The pipeline performs several data cleaning steps:

- Remove duplicate rows
- Fill missing values
  - Director → `Unknown`
  - Country → `Unknown`
  - Rating → `Unknown`
- Select only the required columns:
  - show_id
  - type
  - title
  - director
  - country
  - release_year
  - rating
  - duration
  - listed_in

### 3. Load

The cleaned dataset is loaded into PostgreSQL using SQLAlchemy.

Before inserting new records, the pipeline:

- Opens a database transaction
- Truncates the existing table
- Loads the latest dataset

This makes the ETL process **idempotent**, meaning it can be run multiple times while producing the same final database state.

---

## 🗄️ Database Schema

```sql
CREATE TABLE movies (
    show_id VARCHAR(10) PRIMARY KEY,
    type VARCHAR(20),
    title TEXT,
    director TEXT,
    country TEXT,
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(50),
    listed_in TEXT
);
```

---

## 📊 Sample Output

```text
Final shape: (6234, 9)

2026-07-21 11:59:52 - INFO - Connected to PostgreSQL successfully.
2026-07-21 11:59:52 - INFO - Movies table cleared.
2026-07-21 11:59:52 - INFO - Data loaded successfully.
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/abhirajgm1924-sys/movie-data-pipeline.git
cd movie-data-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=movie_pipeline
```

### 5. Create the PostgreSQL database

```sql
CREATE DATABASE movie_pipeline;
```

Create the `movies` table using the schema shown above.

### 6. Run the ETL pipeline

```bash
python src/load.py
```

---

## 📈 Skills Demonstrated

- ETL Pipeline Development
- Data Cleaning with Pandas
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Environment Variable Management
- Logging
- Transaction Management
- Idempotent Data Pipelines
- Python Programming
- SQL

---

## 🔮 Future Improvements

- Add automated unit tests
- Dockerize the application
- Build a FastAPI service
- Schedule ETL jobs using Apache Airflow
- Support incremental data loading
- Add data validation with Great Expectations

---

##  Authors

Haritha Thurpati
Abhiraj Pittala

GitHub: https://github.com/harithagm2419
GitHub: https://github.com/abhirajgm1924



---

## License

This project is intended for educational and portfolio purposes.