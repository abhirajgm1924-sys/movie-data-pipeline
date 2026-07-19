from database.connection import get_connection

def get_all_movies():
    con=get_connection()
    cur=con.cursor()

    cur.execute("SELECT * FROM netflix_titles;")
    movies=cur.fetchall()

    cur.close()
    con.close()

    return movies

def count_movies():
    con=get_connection()
    cur=con.cursor()

    cur.execute("SELECT COUNT(*) FROM netflix_titles;")
    count=cur.fetchone()[0]

    cur.close()
    con.close()

    return count

def find_by_title(title):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM netflix_titles
        WHERE title ILIKE %s;
        """,
        (f"%{title}%",)
    )

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result

def movies_by_country(country):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT title, release_year
        FROM netflix_titles
        WHERE country ILIKE %s;
        """,
        (f"%{country}%",)
    )

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result


def movies_by_rating(rating):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT title
        FROM netflix_titles
        WHERE rating = %s;
        """,
        (rating,)
    )

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result
