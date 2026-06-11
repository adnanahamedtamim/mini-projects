
while True :
    yn=input("do you like to continue ? y/n :").lower()
    if yn=='n' : 
        break
    
    try :
        a=float(input("enter first number :"))
        sign=input("enter the ops you want to do +,-,*,/,** :")
        b=float(input("enter second number :"))    
        res=-1
            
        if sign=='+' :
            res=a+b 
        elif sign=='-' :
            res=a-b
        elif sign=='*' :
            res=a*b
        elif sign=='**' :
            res=a**b
        elif sign=='/' :
            if b==0 :
                print("undefined")
            else :
                res=a/b 
        else : 
            print("undefines operator")
            # continue

        if res!=-1 : 
            print("result :" + str(res))  
    except ValueError :
            print("please enter valid input")    
