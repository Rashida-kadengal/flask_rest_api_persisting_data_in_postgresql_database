import psycopg2
conn=psycopg2.connect(
    dsn='postgresql://postgres:password@localhost:5432/assignment_flask_db'
)