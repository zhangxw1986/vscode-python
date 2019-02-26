# -*- coding: utf-8 -*-
import sys
import io
import mysql.connector
#改变标准输出的默认编码,windows需要加这个
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

if __name__ == "__main__":
  # conn =sqlite3.connect('test.db')
  # cursor = conn.cursor()
  # # cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
  # cursor.execute('insert into user (id,name) values (\'2\',\'rid\')')
  # rc = cursor.rowcount
  # print(rc)
  # cursor.execute('select * from user where id =?',('1',))
  # values =  cursor.fetchall()
  # print(values)

  # cursor.close()
  # conn.commit()
  # conn.close()

  conn = mysql.connector.connect(user='root',password='zh123456',database='test')
  cursor = conn.cursor()
  # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
  cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Kate'])
  cursor.execute('select * from user where id=%s',('2',))
  value = cursor.fetchall()
  print(value)
  cursor.rowcount
  conn.commit()
  cursor.close()
  conn.close()