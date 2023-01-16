import conn as c
class Registration:
    def getr(self):
        self._rno=int(input("Enter Rollno. :"))
        self._name=input("Enter Name :")
        self._age=int(input("Enter Age :"))
        self._city=input("Enter City :")
        self._mobile=int(input("Enter Mobile No. :"))
        self._email=input("Enter Email Id :")
    def __show__(self):
         print("Rollno.:",self._rno)
         print("Name:",self._name)
         print("Age:",self._age)
         print("City",self._city)
         print("Mobile:",self._mobile)
         print("Email:",self._email)



class Marks:
    def getm(self):
        self._phy=int(input("Enter Marks in Physics :"))
        self._chem=int(input("Enter Marks in Chemistry :"))
        self._math=int(input("Enter Marks in Maths :"))
        self._eng=int(input("Enter Marks in English :"))
        self._hin=int(input("Enter Marks in Hindi :"))

    def __show__(self):
         print("Marks in Physics:",self._phy)
         print("Marks in Chemistry:",self._chem)
         print("Marks in Maths:",self._math)
         print("Marks in English:",self._eng)
         print("Marks in Hindi:",self._hin)

class Result(Registration,Marks):
    def calculate(self):
        
        Registration.getr(self)   #call Constructor of Registration Class
        Marks.getm(self)   ##call Constructor of Marks Class
        self.__total=self._phy+self._chem+self._math+self._eng+self._hin
        m=0
        if self._phy<40:
            m=m+1
        if self._chem<40:
            m=m+1
        if self._math<40:
            m=m+1    
        if self._eng<40:
            m=m+1
        if self._hin<40:
            m=m+1         
        if m==0:
            self.__remark='PASS'
            self.__percent=self.__total/500*100
            #print("Percentage:",self.__percent)
            if self.__percent>=80:
                self.__grade='A+'
            elif self.__percent<80 and self.__percent>=70:
                self.__grade='A'
            elif self.__percent<70 and self.__percent>=60:
                self.__grade='+B'
            elif self.__percent<60 and self.__percent>=50:
                self.__grade='B'
            else:
                self.grade='C'
        elif m==1 or m==2:
            self.__remark='Supplymentary'
            self.__grade=''
            self.__percent=''
            
        else:
            self.__remark='Fail'
            self.__grade=''
            self.__percent=''
        
    def insert(self):
#create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        query="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self._rno,self._name,self._age,self._city,self._mobile,self._email,self._phy,self._chem,self._math,self._eng,self._hin,self.__total,self.__percent,self.__grade,self.__remark)
        try:
            #create cursor
            cur=conn.cursor()
            cur.execute(query,val)
        except Exception as e1:
            print("Query Error")
            #print(e1)
        else:
            conn.commit()
            print("Record Save Successfully")
            conn.close()
            
    def delete(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno to delete:"))
        query=("delete from student where rno=%s")
        try:
            
            #create cursor
            cur=conn.cursor()
            cur.execute(query,r)
        except Exception as e2:
            print("Query Error")
                
        else:
            conn.commit()
            print("Record Deleted Successfully")
            conn.close()
        
        
    def search(self):
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno to Search:"))
        query=("select * from student where rno=%s")
        try:
            
            #create cursor
            cur=conn.cursor()
            cur.execute(query,r)
        except Exception as e3:
            print("Query Error")
                
        else:
            stud=cur.fetchall()
            if stud:
                for i in stud:
                    print("Roll no:",i[0])
                    print("Name:",i[1])
                    print("Age:",i[2])
                    print("City:",i[3])
                    print("Mobile:",i[4])
                    print("Email:",i[5])
                    print("Marks in Physics:",i[6])
                    print("Marks in Chemistry:",i[7])
                    print("Marks in Maths:",i[8])
                    print("Marks in English:",i[9])
                    print("Marks in Hindi:",i[10])
                    print("Total Marks:",i[11])
                    print("Percentage:",i[12])
                    print("Grade:",i[13])
                    print("Remark:",i[14])
                    
            else:
                print("Roll no.{} doesn't exist".format(r))
            conn.close()
        
    
    def update_name(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno:"))
        n=input("Enter Update Name:")
        query=("update student set name=%s where rno=%s")
        try:
            val=(n,r)
            #create cursor
            cur=conn.cursor()
            cur.execute(query,val)
        except Exception as e4:
            print("Query Error")
            print(e4)
                
        else:
            print("Record Update Successfully")
            conn.commit()
            conn.close()

    def update_age(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno:"))
        a=int(input("Enter update Age:"))
        query=("update student set age=%s where rno=%s")
        try:
            val=(a,r)
            #create cursor
            cur=conn.cursor()
            cur.execute(query,val)
        except Exception as e5:
            print("Query Error")
            
                
        else:
            print("Record Update Successfully")
            conn.commit()
            conn.close()

    def update_city(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno:"))
        cy=input("Enter update City:")
        query=("update student set city=%s where rno=%s")
        try:
            val=(cy,r)
            #create cursor
            cur=conn.cursor()
            cur.execute(query,val)
        except Exception as e6:
            print("Query Error")
            
                
        else:
            print("Record Update Successfully")
            conn.commit()
            conn.close()

    def update_mobile(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno:"))
        num=int(input("Enter update Mobile:"))
        query=("update student set mobile=%s where rno=%s")
        try:
            val=(num,r)
            #create cursor
            cur=conn.cursor()
            cur.execute(query,val)
        except Exception as e7:
            print("Query Error")
            
                
        else:
            print("Record Update Successfully")
            conn.commit()
            conn.close()                   
    def update_email(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        r=int(input("Enter Rollno:"))
        em=input("Enter update Email:")
        query=("update student set email=%s where rno=%s")
        try:
            val=(em,r)
            #create cursor
            cur=conn.cursor()
            cur.execute(query,val)
        except Exception as e7:
            print("Query Error")
            
                
        else:
            print("Record Update Successfully")
            conn.commit()
            conn.close()

    def display(self):
        #create the object of class
        c1=c.Connection1()
        conn=c1.getconnection()
        query=("select * from student")
        try:
            
            #create cursor
            cur=conn.cursor()
            cur.execute(query)
        except Exception as e2:
            print("Query Error")
                
        else:
            stud=cur.fetchall()
            for i in stud:
                print("Roll no:",i[0])
                print("Name:",i[1])
                print("Age:",i[2])
                print("City:",i[3])
                print("Mobile:",i[4])
                print("Email:",i[5])
                print("Marks in Physics:",i[6])
                print("Marks in Chemistry:",i[7])
                print("Marks in Maths:",i[8])
                print("Marks in English:",i[9])
                print("Marks in Hindi:",i[10])
                print("Total Marks:",i[11])
                print("Percentage:",i[12])
                print("Grade:",i[13])
                print("Remark:",i[14])
                    
                    
            
            conn.commit()
            conn.close()
            
    
#main program
res=Result()
print("1.Insert Student Details:")
print("2.Delete Student Details:")
print("3.Search Student Details:")
print("4.Update Student Details:")
print("5.Display All Students Detials:")

ch=int(input("Enter Your Choice:"))


if ch==1:
    res.calculate()
    res.insert()
elif ch==2:
    res.delete()
elif ch==3:
    res.search()
elif ch==4:
    print("1.Update Student Name")
    print("2.Update Student Age")
    print("3.Update Student City")
    print("4.Update Student Mobile")
    print("5.Update Student Email")
    ch1=int(input("Enter Your Choice:"))
    if ch1==1:
        res.update_name()
    elif ch1==2:
        res.update_age()
    elif ch1==3:
        res.update_city()
    elif ch1==4:
        res.update_mobile()
    elif ch1==5:
        res.update_email()    

elif ch==5:
    res.display()
else:
    print("Invalid Choice")
