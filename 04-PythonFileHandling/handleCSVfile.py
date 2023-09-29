import csv
with open("emp.csv","w",newline='') as f:
    #open file/create file to write
    w = csv.writer(f) #return csv writer object

    #write to file using writerow
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n = int(input("Enter number of employee:"))

    for i in range(n):
        eno = int(input("Enter employee number:"))
        ename = input("Enter employee name:")
        esal = int(input("Enter employee salary:"))
        eaddr = input("Enter employee address:")

        w.writerow([eno,ename,esal,eaddr])

print("Data entered Successfully!!!")

#=================================================

import csv
with open("emp.csv",'r') as f:
    r = csv.reader(f)
    data = list(r)
    #print(data[1])


    #PRINT DATA IN TABULAR FORM
    for line in data:
        for data in line:
            print(data,"   ",end="")
        print("\n")
    
    
    #print list of employee names
    names = []
    info = []
    for line2 in data[1:4]:
        names.append(line2[1])
        info.append(line2[0]+line2[1])

    print(names)
    print(info)

    f.close()
#----------------------------------------------------
    for dat in r:
        print(dat[0]," ",dat[1]," ",dat[2]," ",dat[3])
        print("\n")
    f.close()

#====================================================
import csv
  
# Open the CSV file for reading
with open('emp.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    print(type(csv_reader))
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        print(row)