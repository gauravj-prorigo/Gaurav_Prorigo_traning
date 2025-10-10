exp = input("enter the excepration :")
allowed = "0123456789+-*/(). "
safe = True
for i in exp:
    if i not in allowed:
        safe = False
        print("Invalid input !!!!")
        break
    
if safe:
    result = eval(exp)
    print("The result is : ",result)    
        
