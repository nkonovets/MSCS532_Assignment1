


def get_data(filename): 
    filename = filename

    with open(filename, "r") as file:
        data_line = file.readline()

    str_list = data_line.split(",")

    num_data = []

    for i in str_list:
        num_data.append(int(i))

    return num_data



def insertion_sort_algorithm(unsorted_list):
    tosort = unsorted_list

    for i in range(1, len(tosort)): #2,4,6,1,3

        key = tosort[i] #4
        j = i - 1 #j = 0

        while j >= 0 and tosort[j] < key: #tosort[0] (2) < (4)

            tosort[j+1] = tosort[j] #tosort[1] (4) = tosort[0] (2)

            j = j - 1 #(-1)

        tosort[j + 1] = key #j = (1), tosort[1] (2) = (4) 
        

    sorted_data = tosort
    return sorted_data



unsorted_data = get_data(input("Specify the file to get data from: "))
print("Input data: " + str(unsorted_data) + "\n \n")

sorted_data = insertion_sort_algorithm(unsorted_data)
print("Data after sorting: " + str(sorted_data) + "\n \n")


            


    
        




    



