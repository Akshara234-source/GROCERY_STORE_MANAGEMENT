
import mysql.connector as con
db=con.connect(host="localhost",user="root",password="Riya@2310",database="Grocery_Store")
cur=db.cursor()
print("Database connected successfully")
def show():
    cur.execute("select * from g_store")
    rec=cur.fetchall()
    print("Product_ID","\t","Product_Name","\t\t","Quantity","\t\t","Cost_Price","\t","Selling_Price","\t","Profit")
    for i in range (len(rec)):
        print(rec[i][0],"\t\t",rec[i][1],"\t\t\t",rec[i][2],"\t\t",rec[i][3],"\t\t",rec[i][4],"\t\t",rec[i][5])
        

def add():
    print("Enter details to be added")
    pid=int(input("Enter product id:"))
    pname=input("Enter product name:")
    quantity=int(input("Enter product quantity:"))
    cp=float(input("Enter cost price:"))
    sp=float(input("Enter selling price:"))
    profit=float(input("Enter profit:"))
    cur.execute("insert into g_store values({},'{}',{},{},{},{})".format(pid,pname,quantity,cp,sp,profit))
    db.commit()
    print("Item has been added successfully")

def update():
    print("Enter details to be updated")
    pid=int(input("Enter product id:"))
    quantity=int(input("Enter new product quantity:"))
    cur.execute("update g_store set quantity={} where product_id={}".format(quantity,pid))
    db.commit()
    print("Item has been updated successfully")

def delete():
     print("Enter data to be deleted")
     pid=int(input("Enter product id:"))
     cur.execute("delete from g_store where product_id={}".format(pid))
     db.commit()
     print("Item has been deleted successfully")

while True:
    print("1.To display all records")
    print("2.To add record")
    print("3.To update record")
    print("4.To delete record")
    print("5.To exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        show()
        print("\n=======================================================================================")
    elif ch==2:
        add()
        print("\n=======================================================================================")
    elif ch==3:
        update()
        print("\n=======================================================================================")
    elif ch==4:
        delete()
        print("\n=======================================================================================")
    elif ch==5:
         break
    else:
        print("Invalid choice. Please try again")
        print("\n=======================================================================================")

cur.close()
db.close()



