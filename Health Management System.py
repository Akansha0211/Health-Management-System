# Health Management System
# Total 6 Files, 3 For exercise and 3 For for diet
# 3 clients - SHIVAM, SHUBHAM and SATYAM
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client


#DESCRIPTION :
"""You are a NUTRIONIST  and you need give your patients a software on which they can keep thier track of whatever food (log thier food)they took and whatever eexercise they performed which you can retrieve later """

def getdate():
    import datetime
    return datetime.datetime.now()

def add_log(n):
    if n==1:
        ex_diet=int(input("Enter what you want to log\n"
                      "1 for diet\n"
                      "2 for exercise"))
        if ex_diet==1:
            diet=input("Enter your diet")
            with open("Shubham_food.txt","a")as f:
                f.write(str(getdate())+diet + "\n")
            print("You have entered your diet")
        if ex_diet==2:
            ex=input("Enter your exercise")
            with open("Shubham_ex","a") as g:
                g.write(str(getdate())+ex+"\n")
            print("You have entered your exercise")
    if n==2:
        ex_diet = int(input("Enter what you want to log\n"
                            "1 for diet\n"
                            "2 for exercise"))
        if ex_diet==1:
                diet = input("Enter your diet")
                with open("Shivam_food.txt", "a")as f:
                    f.write(str(getdate()) + diet + "\n")
                print("You have entered your diet")
        if ex_diet == 2:
                ex = input("Enter your exercise")
                with open("Shivam_ex", "a") as g:
                    g.write(str(getdate())+ex + "\n")
                print("You have entered your exercise")
    if n==3:
        ex_diet = int(input("Enter what you want to log\n"
                            "1 for diet\n"
                            "2 for exercise"))
        if ex_diet == 1:
            diet = input("Enter your diet")
            with open("Satyam_food.txt", "a")as f:
                f.write(str(getdate()) + diet + "\n")
            print("You have entered your diet")
        if ex_diet == 2:
            ex = input("Enter your exercise")
            with open("Satyam_ex", "a") as g:
                g.write(str(getdate())+ex + "\n")
            print("You have entered your exercise")
def retrieve(n):
    if n==1:
        ex_diet=int(input("Enter what you want to retrieve\n"
                      "1 for diet\n"
                      "2 for exercise"))
        if ex_diet==1:
            with open("Shubham_food.txt")as f:
                print(f.read())
        if ex_diet==2:
            with open("Shubham_ex.txt") as g:
                print(g.read())
    if n==2:
        ex_diet = int(input("Enter what you want to retrieve\n"
                            "1 for diet\n"
                            "2 for exercise"))
        if ex_diet==1:
                with open("Shivam_food.txt")as f:
                    print(f.read())
        if ex_diet == 2:
                with open("Shivam_ex") as g:
                    print(g.read())

    if n==3:
        ex_diet = int(input("Enter what you want to log\n"
                            "1 for diet\n"
                            "2 for exercise"))
        if ex_diet == 1:
            with open("Satyam_food.txt")as f:
                print(f.read())
        if ex_diet == 2:
            with open("Satyam_ex.txt") as g:
                print(g.read())

print("WELCOME TO THE HEALTH MANAGEMENT SYSTEM")
log_ret=int(input("Enter 1 to log \n"
            "2 to retrieve:\n"))
name = int(input("Enter 1 for Shubham\n"
               "2 for Shivam\n"
               "3 for Satyam"))
if log_ret==1:
    add_log(name)
else:
    retrieve(name)


