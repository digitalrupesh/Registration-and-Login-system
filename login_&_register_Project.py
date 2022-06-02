def register():
    db=open("user_database.txt","r")
    user=input("Create a Username: ")
    user=user.lower()
    username=user
    while "@" not in username:
            username = input("Your email address must have '@' in it\nPlease write your email address again: ")
            if len(username) <= 6 :
                username = input("Your email address is too short\nPlease write your email address again: ")
            if "." not in username:
                username = input("Your email address must have '.' in it\nPlease write your email address again: ")
    while "." not in username:
                username = input("Your email address must have '.' in it\nPlease write your email address again: ")
                if len(username) <= 6 :
                    username = input("Your email address is too short\nPlease write your email address again: ")
                if "@" not in username:
                    username = input("Your email address must have '@' in it\nPlease write your email address again: ")

    password=input("Create a Passowrd: ")
    password1=input("Confirm a Password: ")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(", ")
        b=b.strip()
        d.append(a)
        f.append(b)
    data =dict(zip(d, f))

    if password != password1:
        print("Password does not match")
        register()    
    else:
        if len(password)<=6:
            print("Password is too short")
            register()
        elif username in d:
            print("Username is already exist please choose another one!")
            register()
        else:
            db=open("user_database.txt","a")
            db.write(username+", "+password+"\n")
            print("success!")


def access():
    db=open("user_database.txt","r")
    username=input("Enter a username: ")
    password=input("Enter a Password: ")

    if not len(username or password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))
       
        try:
            if data[username]:
                try:
                    if password==data[username]:
                        print("Login success")
                        print("Hi,",username)
                    else:
                        print("Password or Username incorrect")
                except:
                    print("incorrrect passowrd or Username")
            else:
                print("username or password doesn't exist")
        except:
            print("username and passowrd doesnot Exit")
    else:
        print("Please enter a value")

def home(option=None):
    option=input("Login| signup: ")
    if option == "Login":
        access()
    elif option == "signup":
        register()
    else:
        print("Please enter an options")
home()
    

    


