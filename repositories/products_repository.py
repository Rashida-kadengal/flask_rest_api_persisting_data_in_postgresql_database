from db.db_conn import conn

class ProductRepository:
    def fetch_all_products(self):
        try:
            cur=conn.cursor()
            cur.execute("select id,name,created_at from product")
            rows=cur.fetchall()
            products=[{"id":row[0],"name":row[1]} for row in rows]
            return products
        except Exception as e:
            print(e)
            return None
        finally:
            cur.close()

    def fetch_product_by_id(self,product_id):
        try:
            cur=conn.cursor()
            cur.execute("select id,name from product where id=%s",(product_id,))
            data=cur.fetchone()
            if data:
                product={
                    "id":data[0],
                    "name":data[1]
                }
                return product
            else:
                return None
        finally:
            cur.close()


    def add_product(self,name):
        try:
            cur=conn.cursor()
            cur.execute("insert into product(name) values(%s) RETURNING id",(name,))
            data=cur.fetchone()
            conn.commit()
            return data[0]
        except Exception as e:
            print(e)
            return None
        finally:
            conn.rollback()
            cur.close


    def update_product_data(self,product_id,new_name):
        try:
            cur=conn.cursor()
            cur.execute("update product set name=%s where id=%s",(new_name,product_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()


    def delete_product_data(self,product_id):
        try:
            cur=conn.cursor()
            cur.execute("delete from product where id=%s",(product_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()



