phDictionry ={}

def phonebook(name,email,phone):
    phDictionry[name] = {"Name":name,"email":email,"phone":phone}

def showbook():
    if phDictionry:
     for name in phDictionry.values():
       print(name)
    else:
        print("Its empty !!")
           
        
# phonebook("Gaurav","gauravjadhav@gmail.com",9420404712) 
# phonebook("saurav","sauravYadhav@gmail.com",9420404712)  

n = int(input("Enter the how many contact you wann add : ")) 

# for i in range(n):
#     print("Enter thw contact details of conatct ",i+1)
#     name = (input("Name :"))   
#     email = (input("Email :"))
#     phone = (input("phone :")) 
#     phonebook(name,email,phone)


for i in range(n):
    print("Enter thw contact details of conatct ",i+1)
    name = (input("Name :"))
    while True:
         email = (input("Email :"))
         if "@" in email and "." in email and email.index("@") < email.rindex(".") and email.endswith(".com"):
            break
         else:
            print("Invalid email!")    
            
    while True:
        phone = (input("phone :")) 
        if phone.isdigit() and len(phone) <= 10:
            break
        else:
            print("Invalid phone!")             
   
    
    phonebook(name,email,phone)
            
showbook()