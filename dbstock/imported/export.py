from openpyxl import Workbook #class สร้างไฟล์ excel
import sqlite3
import mysql.connector

con = sqlite3.connect('stockdb.db')
cursur = con.cursor()
data = '''
      select unit
      from products
      GROUP BY unit;
'''
cursur.execute(data)
product = cursur.fetchall()  #เก็บข้อมูลจาก cursur ทั้งหมดให้อยู่ในนี้

#excel
workbook = Workbook()
sheet = workbook.active
sheet.append(['ชื่อ']) #insert data

for p in product:
    print(p)
    sheet.append(p)

workbook.save(filename= 'exportedProduct.xlsx')