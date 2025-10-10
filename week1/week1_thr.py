phDictionry ={}

def phonebook(name,email,phone):
    phDictionry[name] = {"Name":name,"email":email,"phone":phone}

def showbook():
    if phDictionry:
     for name in phDictionry.values():
       print(name)
    else:
        print("Its empty !!")
           
        
# phonebook() 
# phonebook("saurav","sauravYadhav@gmail.com",9420404712)            
showbook()