#!/usr/local/bin/python3.7
import image

import mysql.connector


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
  cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Jack'])
  cursor.execute('select * from user where id=%s',('1',))
  value = cursor.fetchall()
  print(value)
  cursor.rowcount
  conn.commit()
  cursor.close()
  conn.close()