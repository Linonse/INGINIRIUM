def ask_password(true_password):
    #считывание переменной
    pas=input()
    a=1
    while pas!=true_password and a<3:
        pas=input()
        a+=1
    if pas==true_password:
        print("UNLOCKED")
    else:
        print("BLOCKED")

true_password=123456
ask_password(true_password)