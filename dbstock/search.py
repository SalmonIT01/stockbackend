import sqlite3

con = sqlite3.connect('stockdb.db')
cursur = con.cursor()

def search():
    user_input = input('Search:')
    try:
        int(user_input)
        search_sql = '''SELECT * FROM products2
        WHERE product_id LIKE "%{0}%" '''.format(user_input)
        
    except :
        search_sql = '''SELECT * FROM products2
        WHERE product_name LIKE "%{0}%" '''.format(user_input)

    cursur.execute(search_sql)
    result = cursur.fetchall()
    print(result)
   

def insert():
    print("INSERT")
    input_id = input('product id:')
    input_title = input('product name')
    input_unit = int(input('unit:'))
    input_amount = float(input('amount:'))
    
    insert_sql = '''INSERT INTO products2 (product_id,product_name,unit_id,amount)
                     VALUES("{0}","{1}","{2}","{3}")'''.format(input_id,input_title,input_unit,input_amount)
    
    cursur.execute(insert_sql)
    con.commit()
    convert_time(input_id) #function convert time
    showdb()
    
def showdb():
    db = '''SELECT * 
            FROM products2; '''
    cursur.execute(db)
    product_table = cursur.fetchall()
    print(product_table)

def updatedb():
    search()
    user_input = input('select data to update[product id]:')
    input_title = input('product name')
    input_unit = int(input('unit:'))
    input_amount = float(input('amount:'))
    
    update_sql = '''
    UPDATE products2
    set product_name= "{0}",unit_id = "{1}", amount= "{2}"
    WHERE product_id = "{3}";
    '''.format(input_title,input_unit,input_amount,user_input)
    cursur.execute(update_sql)
    con.commit()
    
def convert_time(p_id):
    sql_date = '''
            select datetime(create_date, 'localtime')
            from products2
            where product_id = "{0}";'''.format(p_id)
    cursur.execute(sql_date)
    date_list = cursur.fetchall()
    datenow = date_list[0][0]
    
    update = '''
          UPDATE products2
          set create_date = '{0}'
          where product_id = {1};
    '''.format(datenow,p_id)
    
    cursur.execute(update)
    con.commit()
    

    
    
    
    
print("kk")    
# search()    

# showdb()  
# insert()  
# updatedb()
