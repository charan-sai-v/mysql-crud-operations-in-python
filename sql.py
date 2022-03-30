import mysql.connector

#connection of mysql
mydb = mysql.connector.connect(
  host="your_host", 
  user="your_name",
  password="your_password"
)

#creating a cursor object
mycursor = mydb.cursor()
mycursor.execute("Show databases")
databases = mycursor.fetchall()
for i in databases:
    print(i)
    

data = input("Enter Database: ")
mycursor.execute(f"USE {data}")

print("Welcome to MENU")
print("Select the options \n 1. CREATE TABLE \n 2. INSERT VALUES \n 3. Display the values\n 4. Updating values\n 5. Deleting values\n 6. Exit")

va = True

while va:
    value = int(input("Enter your option: "))
    try:
        #Creating a table
        if value == 1:
            table_name = input("Enter the table name: ")
            #creating  table
            mycursor.execute(f"CREATE table {table_name}(id int primary key NOT NULL, name varchar(30), price int);")
            print("Table Created Successfully...")
        
        #Inserting a values
        elif value == 2:
            pid = int(input("Enter the id: "))
            name = input("Enter the name: ")
            price = int(input("Enter the price: "))
            
            #inserting values
            mycursor.execute(f"INSERT into store_product values({pid}, '{name}', {price})")
            mydb.commit()
            print("Successfully")
           
        #Displays the values  
        elif value == 3:
            
            mycursor.execute("select * from store_product;")
            
            result = mycursor.fetchall()
            
            for i in result:
                 id = i[0]
                 name = i[1]
                 price = i[2]
                 print(id, name, price)
                 
        #Updating values          
        elif value == 4:
            
            update_name = input("Enter the name to update: ")
            update_price = input("Enter the price to update: ")
            mycursor.execute(f"UPDATE store_product SET name='{update_name}', price={update_price} WHERE id=101")
            mydb.commit()
            print("Records are updates successfully........")
            
        #Deleting values
        elif value == 5:
            
            delete_id = int(input("Enter the id to delete the value: "))
            mycursor.execute(f"DELETE FROM store_product WHERE id={delete_id}")
            mydb.commit()
            print("Record deleted successfully....")
            
        elif value == 6:
            print("You were exited")
            va = False
            
        
            

    except:  
      # rollback used for if any error   
      mydb.rollback()  
    
mydb.close()#Connection Close  
