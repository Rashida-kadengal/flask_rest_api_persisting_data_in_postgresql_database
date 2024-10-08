from db.db_conn import conn
class BrandRepository:
    def fetch_all_brands(self):
        try:
            cur=conn.cursor()
            cur.execute("select id,name from brand")
            rows=cur.fetchall()
            brands=[{"id":row[0],"name":row[1]} for row in rows]
            return brands
        except Exception as e:
            print(e)
            return None
        finally:
            cur.close()


    def fetch_brand_by_id(self,brand_id):
        try:
            cur=conn.cursor()
            cur.execute("select id,name from brand where id=%s",(brand_id,))
            data=cur.fetchone()
            if data:
                brands={
                    "id":data[0],
                    "name":data[1]
                }
                return brands
            else:
                return None
        finally:
            cur.close()



    def add_brand(self,name):
        try:
            cur=conn.cursor()
            cur.execute("insert into brand(name) values(%s) RETURNING id",(name,))
            data=cur.fetchone()
            conn.commit()
            return data[0]
        except Exception as e:
            print(e)
            return None
        finally:
            conn.rollback()
            cur.close()


    def update_brand_data(self,brand_id,new_name):
        try:
            cur=conn.cursor()
            cur.execute("update brand set name=%s where id=%s",(new_name,brand_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()


    def delete_brand_data(self,brand_id):
        try:
            cur=conn.cursor()
            cur.execute("delete from brand where id=%s",(brand_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()


