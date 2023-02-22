def name_generator(name,petname):
    return name+" "+petname
if __name__ =="__main__":
    a = input("Enter Your Firstname: ")
    b = input("Your First pet name : ")
    c = name_generator(a,b)
    print(f"Your new name is : {c}")