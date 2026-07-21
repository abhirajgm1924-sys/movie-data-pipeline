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