import pandas as pd
import mysql.connector


class Pipeline(object):
    def _init_(self):
      self.create_connection()
      self.create_table()
    def create_connection(self):
      self.conn=mysql.connector.connect(
        host='localhost',
        user='root',
        database='chem'
      )
      self.curr=self.conn.cursor(

      )
    def create_table(self):
       self.curr.execute(""" DROP TABLE IF EXISTS chem_tb """)
       self.curr.execute(""" create table chem_tb(
                         title_change text,
                         author text,
                         tap text                   
       )""")

    def process_item(self,item,spider):
       self.store_db(item)
       return item
    def store_db(self,item):
       self.curr.execute("""insert into chem_tb value (%s,%s,%s) """,(
                         item['title_change'][0],
                         item['author'][0],
                         item['tap'][0]
        ))
       self.conn.commit()
       
