number_string = input("list of numbers seperated by a comma: ")
num_list = number_string.split(",")
int_list = []

for num in num_list:
    int_num = int(num.strip())
    int_list.append(int_num)

for checker in int_list:
    if checker % 2 == 0:
        print(f"{checker} is even")

    elif checker % 2 == 1:
        print (f"{checker} is odd")

    else:
        print ("Invalid number")