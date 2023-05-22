import pymysql
user = 'root'
passw = 'test'
host =  '127.0.0.1'
port = 3306
database = 'mydb'

conn = pymysql.connect(host=host,
                       port=port,
                       user=user, 
                       passwd=passw,  
                       db=database,
                       charset='utf8')

def data_upload(data, table_name):
    data.to_sql(name= table_name, con=conn, if_exists = 'replace', index=False, flavor = 'mysql')