import sqlite3

try:
    mydb = sqlite3.connect('Minor_project.db')
    cursor = mydb.cursor()
    cursor.execute("select * from questions")
    ssum=0
    msum=0
    print("1. Rarely or none of the time (less than 1 day)")
    print("2. Some or a little of the time (1-2 days)")
    print("3. Occasionally or a moderate amount of the time (3-4 days)")
    print("4. Most or all of the time (5-7 days)")
    for i in cursor.fetchall():
        for j in range(0,1):
            qno=i[0]
            ques=i[1]
            query = "Select * from points;"
            print("\nQues %d: %s"%(qno,ques))
            a=int(input("Enter Your Choice from above Options:"))
            if (a==1):
                sql_select_query = """select * from Points where opt = ?"""
                cursor.execute(sql_select_query, (a,))
                pts=cursor.fetchall()
                for row in pts:
                    ssum=ssum+row[1]
            elif (a==2):
                sql_select_query = """select * from Points where opt = ?"""
                cursor.execute(sql_select_query, (a,))
                pts=cursor.fetchall()
                for row in pts:
                    ssum=ssum+row[1]
            elif (a==3):
                sql_select_query = """select * from Points where opt = ?"""
                cursor.execute(sql_select_query, (a,))
                pts=cursor.fetchall()
                for row in pts:
                    ssum=ssum+row[1]
            elif (a==4):
                sql_select_query = """select * from Points where opt = ?"""
                cursor.execute(sql_select_query, (a,))
                pts=cursor.fetchall()
                for row in pts:
                    ssum=ssum+row[1]
            elif (a==5):
                sql_select_query = """select * from Points where opt = ?"""
                cursor.execute(sql_select_query, (a,))
                pts=cursor.fetchall()
                for row in pts:
                    ssum=ssum+row[1]
            
    print("Sum:", ssum)
    if(ssum<=5):
        cursor.execute("select * from low_range_questions")
        print("1. Rarely or none of the time (less than 1 day)")
        print("2. Some or a little of the time (1-2 days)")
        print("3. Occasionally or a moderate amount of the time (3-4 days)")
        print("4. Most or all of the time (5-7 days)")
        for i in cursor.fetchall():
            for j in range(0,1):
                qno=i[0]
                ques=i[1]
                query = "Select * from points;"
                print("\nQues %d: %s"%(qno,ques))
                a=int(input("Enter Your Choice from above Options:"))
                if (a==1):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==2):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==3):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==4):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==5):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
    elif(ssum<=10):
        cursor.execute("select * from mid_range_questions")
        print("1. Rarely or none of the time (less than 1 day)")
        print("2. Some or a little of the time (1-2 days)")
        print("3. Occasionally or a moderate amount of the time (3-4 days)")
        print("4. Most or all of the time (5-7 days)")
        for i in cursor.fetchall():
            for j in range(0,1):
                qno=i[0]
                ques=i[1]
                query = "Select * from points;"
                print("\nQues %d: %s"%(qno,ques))
                a=int(input("Enter Your Choice from above Options:"))
                if (a==1):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==2):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==3):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==4):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==5):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
         
    elif(ssum<=15):
        print("High Mental Health")
        cursor.execute("select * from high_range_questions")
        print("1. Rarely or none of the time (less than 1 day)")
        print("2. Some or a little of the time (1-2 days)")
        print("3. Occasionally or a moderate amount of the time (3-4 days)")
        print("4. Most or all of the time (5-7 days)")
        for i in cursor.fetchall():
            for j in range(0,1):
                qno=i[0]
                ques=i[1]
                query = "Select * from points;"
                print("\nQues %d: %s"%(qno,ques))
                a=int(input("Enter Your Choice from above Options:"))
                if (a==1):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==2):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==3):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==4):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
                elif (a==5):
                    sql_select_query = """select * from Points where opt = ?"""
                    cursor.execute(sql_select_query, (a,))
                    pts=cursor.fetchall()
                    for row in pts:
                        msum=msum+row[1]
    print("Ssum:", ssum)
    print("Msum:", msum)
    print("Max:", (ssum+msum))
except mysql.connector.Error as err:
    print("MySQL Error:", err)



finally:
    # Close the database connection
    if 'mydb' in locals() or 'mydb' in globals():
        mydb.close()
