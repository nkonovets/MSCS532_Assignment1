
file = input("Specify the file to get data from: ")



def get_data(filename): 
    filename = filename

    with open(filename, "r") as file:
        data_line = file.readline()

    str_list = data_line.split(",")

    num_data = []

    for i in str_list:
        num_data.append(int(i))

    return num_data


print(get_data(file))
        




    



