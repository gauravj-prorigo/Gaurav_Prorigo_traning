def is_prime(n):
    if n < 2 :
        return False
    for i in range(2,n) :
        if n % i == 0:
            return False
        
    return True    


num = (input("Enter the numbers separted by , : " ))
num = num.split(",")

print(num)
result = ""
for n in num:
    n = n.strip()
    if not n.isdigit():
        print("invliad input");
        exit()
    
    n = int(n)
    if is_prime(n):
        result += str(n) + ", "
         
if len(result)>0:
     result = result[:-2]
print(result)

