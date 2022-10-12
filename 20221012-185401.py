
#greeting card

def question():
    name_1=input("whats your name = ")
    print(name_1+" such a nice name !!\n")
    
    branch_2=input(name_1+" u re from which branch?=")
    print ("first\n")
    rules =input(name_1 +" you need to answer in yes or no if you understand then write'ok'=")

    if rules!="ok":
       return print (" bye -bye!! "+name_1+" have a nice day👍")
    else:print("ok, i see u are interested for 'QNA'\n")
   
    print("first question:-")
    
    quest1=input(name_1+" are you from Mits gwalior? =")
    if quest1!="yes":
       return print("nice to meet u "+name_1+". u should try again")
    else:print ("woww!!"+name_1+" we are from same college 😁 !!")
    
    print ("second question:-")
    
    quest2=input(name_1+" are u from IT(AIR) branch? =")
    if quest2!="yes":
       return print("sorry for asking "+name_1+" i just remembered you are from:-("+branch_2+") branch .But, anyway!!greeting,"+name_1+" i am your college mate harshvardhan , nice to meet you")
    else:print("woww!!"+name_1+" what a coincidence😲 i am also from that branch😃.\n")
    
    print("last question:-\n")
    
    quest3=input(name_1+" u like this greeting card ?=")
    if quest3!="yes":
       
       return print("ok😅 but, anyway greetings "+name_1+" i am harshvardhan Sahu ☺️ your branch mate")
    else:print("thanks😁, \n greetings " +name_1+", i am harsh vardhan your branch mate , nice to meet u☺️ and welcome to mits.\n") 
    print (" finally\n")
    
    print("WELCOME TO MITS  "+name_1+ " and best wishes for future .😁👍\n" )

question ()