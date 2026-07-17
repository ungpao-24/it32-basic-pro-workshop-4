member_list=[]
def add_member(name_para, age_para, gang_para):
    new_member = {
        "name":name_para,
        "age":age_para,
        "gang":gang_para
    }
    member_list.append(new_member)
    return new_member
while True:

    n=(input("1 for Add member | 2 for Show member | [Any key] Quit: "))
    if n == "1":
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        gang=input("Enter your gang: ")
        add_member(name, age, gang)
        print("Add member successfully!")
    elif n == "2":
        print(member_list)
    else :
        print("exit system")
        break