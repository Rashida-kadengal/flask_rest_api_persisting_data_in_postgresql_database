from db_conn import conn
cur=conn.cursor()
cur.execute("create table product(id serial primary key,name varchar(100) not null,created_at date default current_timestamp)")
cur.execute("create table category(id serial primary key,name varchar(100) not null,created_at date default current_timestamp)")
cur.execute("create table brand(id serial primary key,name varchar(100) not null,created_at date default current_timestamp)")
conn.commit()
cur.close()
conn.close()