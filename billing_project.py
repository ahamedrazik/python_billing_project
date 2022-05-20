#simple calc project using python
from time import sleep
import mysql.connector
import datetime
import pandas as pd



#####################################################################33
def free_schema(data):
    
    calc = (data - 100)
    print("Total Electricity Consumption = ", calc)
    
    if calc == 0:
        print("No cost free according to government schemes")
        calc= 0
        first_cost1 ='null'
        second_cost1 = 'null'
        total1= 0
        x = datetime.datetime.now()
        print("Total consumption cost : ",total1)
        print("Please wait a moment let data is store in database...")
        sleep(4)
        zerodb(data,calc,first_cost1,second_cost1,total1,x)
        
        
    elif  calc >=1 and calc <= 100 :
        #sub1  = 100
        #second1 = calc-sub1; #100
        first_cost1= (calc * 1.5)
        print(f"cost of  units{calc} : ",first_cost1 )
        gst1 = 20
        second_cost1 = 0
        
        total1 = first_cost1 + second_cost1 + gst1
    
        print("Total consumption cost with gst : ",total1)
        
        x = datetime.datetime.now()
        dbunit1(data,calc,first_cost1,second_cost1,total1,x)
    
    else:
        sub = 100
        second = calc-sub; #100
        first_cost= (sub * 2)
        print(f"cost of {sub} units :",first_cost )
    
        second_cost = (second * 3)
        print(f"cost of {second} units : ",second_cost )
        gst = 30
        total = first_cost + second_cost + gst
    
        print("Total consumption cost with gst :",total)
    
        x = datetime.datetime.now()
    
        print("please wait a moment let data is store in database...")
        sleep(4)
        dbstore(data,calc,first_cost,second_cost,total,x)
    
#####################################################################33
def fiveth_catag(data):
    if (data == 500) :
        calc = (data - 100)
        print("Total Electricity Consumption = ", calc) #400
    
        eli = 100
        first = calc-eli; #400-100 = 300
        first_cost= (eli * 3.5)
        print(f"cost of {eli} units",first_cost)
    
        second_cost = (first * 4.6)
        print(f"cost of {first} units ",second_cost )
    
        gst = 40
        total = first_cost + second_cost + gst
    
        print("Total consumption cost with gst ",total)
    
        x = datetime.datetime.now()
    
        print("please wait a moment let data is store in database...")
        sleep(4)
        dbstore(data,calc,first_cost,second_cost,total,x)
    
    else:
        calc = (data - 100)
        print("Total Electricity Consumption = ", calc) #400
    
        eli = 100 # 401
        first_cost= (eli * 3.5)
        print(f"cost of {eli} units : ",first_cost)
        
        first = calc-eli; #301 calc 
        second_cost = (eli * 4.6)
        print(f"cost of {eli} units :",second_cost )
        
        
        third = first - eli # 201 calc
        third_cost = (eli * 4.6)
        print(f"cost of {third} units :",third_cost )
        
        fourth= third - eli # 100
        fourth_cost = (eli * 4.6)
        print(f"cost of {fourth} units :",fourth_cost )
        
        fivth= fourth - eli # 1
        fivth_cost = (fivth * 6.6)
        print(f"cost of {fivth} units : ",fivth_cost ) 
        
        gst = 40
        
        total1 = first_cost + second_cost + third_cost + fourth_cost + fivth_cost + gst
    
        print("Total consumption cost with gst : ",total1)
        first_cost1 = first_cost + third_cost + gst
        second_cost1 = fourth_cost + fivth_cost 
        x = datetime.datetime.now()
    
        print("please wait a moment let data is store in database...")
        sleep(4)
        
        dbunit1(data,calc,first_cost1,second_cost1,total1,x)
        
        
############################################################################   
# database store the data
    
def dbstore(data,calc,first_cost,second_cost,total,x):
    
    mydb = mysql.connector.connect(host="localhost",user="razee",passwd="root",database="electricity_bill_store")
    print("database connected")
    mydata = mydb.cursor(dictionary=True)
    query ="insert into  billing_project (total_unit,total_consumption,first_100_unit,last_unit_cost,total_amount,date_time) values (%s,%s,%s,%s,%s,%s)"
    tuple1 = (data,calc,first_cost,second_cost,total,x)
    mydata.execute(query,tuple1)
    mydb.commit()
    print("inserted successfully")
    viewer()
    
    
def dbunit1(data,calc,first_cost1,second_cost1,total1,x):
    mydb = mysql.connector.connect(host="localhost",user="razee",passwd="root",database="electricity_bill_store")
    print("database connected")
    mydata = mydb.cursor(dictionary=True)
    query ="insert into  billing_project (total_unit,total_consumption,first_100_unit,last_unit_cost,total_amount,date_time) values (%s,%s,%s,%s,%s,%s)"
    tuple2 = (data,calc,first_cost1,second_cost1,total1,x)
    mydata.execute(query,tuple2)
    mydb.commit()
    print("inserted successfully")
    viewer()
    
    
def zerodb(data,calc,first_cost1,second_cost1,total1,x):
    mydb = mysql.connector.connect(host="localhost",user="razee",passwd="root",database="electricity_bill_store")
    print("database connected")
    mydata = mydb.cursor(dictionary=True)
    query ="insert into  billing_project (total_unit,total_consumption,first_100_unit,last_unit_cost,total_amount,date_time) values (%s,%s,%s,%s,%s,%s)"
    tuple3 = (data,calc,first_cost1,second_cost1,total1,x)
    mydata.execute(query,tuple3)
    mydb.commit()
    print("inserted successfully")
    viewer()
   

####################################################################
def search_data():
    print(".............................SEARCHING DASDBOARD...............")
    searchdb = int(input("ENTER THE UNIT TO SEARCH:  "))
    print("wait a few minute please let me search data......")
    sleep(4)
    mydb =mysql.connector.connect(host="localhost",user="razee",passwd="root",database="electricity_bill_store")
    print("connection sucessfull")
    mydata = mydb.cursor(dictionary=True)
    query = """SELECT * FROM `billing_project` WHERE total_unit = %s"""
    mydata.execute(query, (searchdb,))
    records = mydata.fetchall()
    
    print("..........................................DATA VIEW.............................................")
    for row in records:
        id = row["id"]
        data = row["total_unit"]
        calc = row["total_consumption"]
        first_cost = row["first_100_unit"]
        second_cost = row ["last_unit_cost"]
        total = row["total_amount"]
        x = row["date_time"]
        
        
        # Define a dictionary containing employee data
        data = {
                'id':[id], 
                'Total_unit':[data], 
		        'Total_consumption':[calc], 
		        'first_100_unit':[first_cost], 
		        'last_unit_cost':[second_cost], 
                'total_amount':[total], 
                'date_time':[x]} 

# Convert the dictionary into DataFrame
        df = pd.DataFrame(data)

# select two columns
        print(df[['id', 'Total_unit',  'Total_consumption', 'first_100_unit', 'last_unit_cost', 'total_amount', 'date_time' ]])
        
##################################################################################       
    

  
def viewer():
    db = input("IF you want to view the database-> TYPE: Y or you want to enable searach options-> TYPE : N   : ")
    if db == 'Y' :
        print("Fetching data from database.....")
        sleep(5)
        validate()
        print("#####################################")
        print("THANK YOU USEME AGAIN!")
        print("#####################################")
    elif db == 'N':
        db2=input("Do you want to enable search options? type :Enable or NOT Enable :   ")
        if db2 == 'Enable':
            search_data()
        else:
            print("your are in disable state")
        print("#####################################")
        print("THANK YOU USEME AGAIN!")
        print("#####################################")
        exit()
    
    
def validate():
    mydb =mysql.connector.connect(host="localhost",user="razee",passwd="root",database="electricity_bill_store")
    print("connected")
    mydata = mydb.cursor(dictionary=True)
    mydata.execute("select * from billing_project")
    records = mydata.fetchall()
    
    print("..........................................DATA VIEW.............................................")
    for row in records:
        id = row["id"]
        data = row["total_unit"]
        calc = row["total_consumption"]
        first_cost = row["first_100_unit"]
        second_cost = row ["last_unit_cost"]
        total = row["total_amount"]
        x = row["date_time"]
        
        
        # Define a dictionary containing employee data
        data = {
                'id':[id], 
                'Total_unit':[data], 
		        'Total_consumption':[calc], 
		        'first_100_unit':[first_cost], 
		        'last_unit_cost':[second_cost], 
                'total_amount':[total], 
                'date_time':[x]} 

# Convert the dictionary into DataFrame
        df = pd.DataFrame(data)

# select two columns
        print(df[['id', 'Total_unit',  'Total_consumption', 'first_100_unit', 'last_unit_cost', 'total_amount', 'date_time' ]])
        
       
#main function called
####################################################################       
        
if __name__=="__main__":
    
    def calc():
        print("#############################################")
        print("WELCOME TO ELECTRICITY BILLING CALC")
        print("#############################################")
        data = int(input("Enter Unit: "))
        return data
        
    def checker(reg):
        if (reg < 500):
            free_schema(reg)
        else:
            fiveth_catag(reg)         
    reg =calc()
    checker(reg)
   

    