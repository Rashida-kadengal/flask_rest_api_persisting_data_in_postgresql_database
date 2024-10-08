from db.db_conn import conn

class CategoryRepository:
    def fetch_all_categories(self):
            try:
                cur=conn.cursor()
                cur.execute("select id,name,created_at from category")
                rows=cur.fetchall()
                categories=[{"id":row[0],"name":row[1]} for row in rows]
                return categories
            except Exception as e:
                print(e)
                return None
            finally:
                cur.close()

    def fetch_category_by_id(self,category_id):
                try:
                    cur=conn.cursor()
                    cur.execute("select id,name from category where id=%s",(category_id,))
                    data=cur.fetchone()
                    if data:
                        category={
                            "id":data[0],
                            "name":data[1]
                        }
                        return category
                    else:
                        return None
                finally:
                    cur.close()


    def add_category(self,name):
                try:
                    cur=conn.cursor()
                    cur.execute("insert into category(name) values(%s) RETURNING id",(name,))
                    data=cur.fetchone()
                    conn.commit()
                    return data[0]
                except Exception as e:
                    print(e)
                    return None
                finally:
                    conn.rollback()
                    cur.close()




    def update_category_data(self,category_id,new_name):
                try:
                    cur=conn.cursor()
                    cur.execute("update category set name=%s where id=%s",(new_name,category_id))
                    conn.commit()
                    return cur.rowcount
                except Exception as e:
                    conn.rollback()
                    raise e
                finally:
                    cur.close()


    def delete_category_data(self,category_id):
            try:
                cur=conn.cursor()
                cur.execute("delete from category where id=%s",(category_id,))
                conn.commit()
                return cur.rowcount   
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cur.close()


