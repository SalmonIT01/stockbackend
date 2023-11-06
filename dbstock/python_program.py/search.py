import sqlite3
from tabulate import tabulate

con = sqlite3.connect('stockdb.db')
cursur = con.cursor()

def insert():
    print("INSERT")
    input_id = input('product id:')
    input_title = input('product name')
    input_unit = input('unit:')
    convert_unit = convert(input_unit)
    input_amount = float(input('amount:'))
    insert_sql = '''INSERT INTO products2 (product_id, product_name,unit_id, amount)
                     VALUES("{0}","{1}","{2}","{3}")'''.format(input_id,input_title,convert_unit,input_amount)
    #
    cursur.execute(insert_sql)
    con.commit()
    convert_time()
    return input_unit

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
    table(result)
   
def showdb():
    db = '''SELECT * 
            FROM products2; '''
    cursur.execute(db)
    data = cursur.fetchall()
    header = ['id','product_id','name','unit_id','amount','status']
    print(tabulate(data,header))
    
def table(data_table):
    data = data_table
    header = ['id','product_id','name','unit_id','amount','status']
    print(tabulate(data,header))


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
    
def delete():
        deleteuser_input = input('select data to delete[product id]:')
        try:
            int(deleteuser_input)
            userinput_sql = '''SELECT product_id FROM products2'''
            cursur.execute(userinput_sql)
            result = cursur.fetchall()
            list_infomation=[]
            for c in result :
                list_infomation.append(list(c)[0])
            str_information = str(deleteuser_input)
            if str_information in list_infomation :
                bool_input = input("Are you sure you want to delete(Y/N): ")
                if bool_input == "Y" :
                    delete_sql = '''
                    DELETE FROM products2
                    WHERE product_id = "{0}" ;
                    '''.format(deleteuser_input)
                    cursur.execute(delete_sql)
                    con.commit()
                    print("Delete complete.")
                elif bool_input == "N" :
                    print("OK system isn't delete your information.")
            else :
                print("Don't have this product id.")
        
        except :
            print("invalid input must to be integer or don't have in order.")
            delete()

def convert(cv):#เปลี่ยน รีม เป็น 3

    unitID = '''select id from unit_table
         where title_unit GLOB  "{0}"'''.format(cv)
    cursur.execute(unitID)
    result = cursur.fetchall()
    x= list(result[0])
    return x[0]


    
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

def status_update():
    get_sql = '''SELECT product_id , amount , status_id FROM products2''' # get product_id, amount, status_id
    cursur.execute(get_sql)
    result = cursur.fetchall()
    for a in result:
        amount = a[1]
        if amount > 0 :
            update_sql = '''
            UPDATE products2
            set status_id = 1
            WHERE product_id = "{0}";'''.format(a[0])
        if amount <= 0 :
            update_sql = '''
            UPDATE products2
            set status_id = 0
            WHERE product_id = "{0}";'''.format(a[0])
        cursur.execute(update_sql)
        con.commit()
    

    
    
    
    
   
# search()    
# showdb()  
# insert()  
# updatedb()
# status_update()
# delete()

