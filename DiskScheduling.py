import csv

#creating a sample csv file containing disk scheduling requests
with open('DiskSchedulingTest.csv',mode='w',newline='') as testfile:
    writer = csv.writer(testfile)
    writer.writerow(["DS1", "200", "50", "UP", "1", "C - Scan", "95", "180", "34", "119", "11","123", "62", "64"])
    writer.writerow(["DS2", "100", "20", "UP","6", "Look", "10", "22", "20", "2", "40", "6","38"])
    writer.writerow(["DS3", "250", "57", "UP","5", "C - Scan", "32", "56", "12", "89", "240"])
    writer.writerow(["DS4", "250", "20", "DOWN","5", "Look", "32", "56", "12", "89", "240"])

def Scan(record):
    DS_NO = record[0]
    X = int(record[1])
    Y = int(record[2])
    Dir = record[3]
    Z = int(record[4])
    requests = record[6:]

    #convert to int
    for i in range(len(requests)):
        requests[i] = int(requests[i])

    seek=[]
    low=[i for i in requests if i<=Y]
    high = [j for j in requests if j> Y]
    low.sort()
    high.sort()
    low.reverse()

    if (Dir == "UP"):
        for i in high:
            seek.append(i)
        if(low!=[]):
            seek.append(X-1)
        for j in low:
            seek.append(j)

    elif (Dir == "DOWN"):
        for i in low:
            seek.append(i)
        if(high!=[]):
            seek.append(0)
        for j in high:
            seek.append(j)

    else:
        print("In Scan: Direction not valid")

    print("seek sequence for ",DS_NO," :")
    for i in seek:
        print(i)

    cylinder_movement = 0
    cylinder_movement += abs(Y-seek[0])
    for i in range(len(seek)-1):
        cylinder_movement += abs(seek[i] - seek[i+1])

    print("total number of cylinder movement is ", cylinder_movement, "and the total time is ", cylinder_movement*Z)


def C_Scan(record):
    DS_NO = record[0]
    X = int(record[1])
    Y = int(record[2])
    Dir = record[3]
    Z = int(record[4])
    requests = record[6:]

    # convert to int
    for i in range(len(requests)):
        requests[i] = int(requests[i])


    seek = []
    low = [i for i in requests if i <= Y]
    high = [j for j in requests if j > Y]
    low.sort()
    high.sort()

    if(Dir =="UP" ):
        for i in high:
            seek.append(i)
        if(low!=[]):
            seek.append(X-1)
            seek.append(0)
        for j in low:
            seek.append(j)

    elif(Dir == "DOWN"):
        low.reverse()
        high.reverse()
        for i in low:
            seek.append(i)
        if(high!=[]):
            seek.append(0)
            seek.append(X-1)
        for j in high:
            seek.append(j)

    else:
        print("In Scan: Direction not valid")

    print("seek sequence for ", DS_NO, " :")
    for i in seek:
        print(i)

    cylinder_movement = 0
    cylinder_movement += abs(Y - seek[0])
    for i in range(len(seek) - 1):
        cylinder_movement += abs(seek[i] - seek[i + 1])

    #should not count when cylinder moves from end to begining or vice versa
    if(X-1 in seek or 0 in seek):
        cylinder_movement -= X-1
    print("total number of cylinder movement is ", cylinder_movement, "and the total time is ", cylinder_movement * Z)


def Look(record):
    DS_NO = record[0]
    X = int(record[1])
    Y = int(record[2])
    Dir = record[3]
    Z = int(record[4])
    requests = record[6:]

    #convert to int
    for i in range(len(requests)):
        requests[i] = int(requests[i])

    seek=[]
    low=[i for i in requests if i<=Y]
    high = [j for j in requests if j> Y]
    low.sort()
    high.sort()
    low.reverse()

    if (Dir == "UP"):
        for i in high:
            seek.append(i)

        for j in low:
            seek.append(j)

    elif (Dir == "DOWN"):
        for i in low:
            seek.append(i)

        for j in high:
            seek.append(j)

    else:
        print("In Scan: Direction not valid")

    print("seek sequence for",DS_NO,":")
    for i in seek:
        print(i)

    cylinder_movement = 0
    cylinder_movement += abs(Y-seek[0])
    for i in range(len(seek)-1):
        cylinder_movement += abs(seek[i] - seek[i+1])

    print("total number of cylinder movement is ", cylinder_movement, "and the total time is ", cylinder_movement*Z)



def C_Look(record):
    DS_NO = record[0]
    X = int(record[1])
    Y = int(record[2])
    Dir = record[3]
    Z = int(record[4])
    requests = record[6:]

    # convert to int
    for i in range(len(requests)):
        requests[i] = int(requests[i])


    seek = []
    low = [i for i in requests if i <= Y]
    high = [j for j in requests if j > Y]
    low.sort()
    high.sort()

    if(Dir =="UP" ):
        for i in high:
            seek.append(i)

        for j in low:
            seek.append(j)

    elif(Dir == "DOWN"):
        low.reverse()
        high.reverse()
        for i in low:
            seek.append(i)

        for j in high:
            seek.append(j)

    else:
        print("In Scan: Direction not valid")

    print("seek sequence for ", DS_NO, ":")
    for i in seek:
        print(i)

    cylinder_movement = 0
    cylinder_movement += abs(Y - seek[0])
    for i in range(len(seek) - 1):
        cylinder_movement += abs(seek[i] - seek[i + 1])


    print("total number of cylinder movement is ", cylinder_movement, "and the total time is ", cylinder_movement * Z)


def start():
    with open('DiskSchedulingTest.csv', 'r', newline='') as readfile:
        reader = csv.reader(readfile)
        for record in reader:
            print("\n\n")
            print(f'{"DS NO.":<8}{"X":<7}{"Y":<7}{"Dir":<7}{"Z":<5}{"Algorithm":<12}{"requests":<10}')
            DS_NO = record[0]
            X = record[1]   #0 to x-1 cylinder
            Y = record[2]   #initial head
            Dir = record[3]
            Z = record[4]   #z milisecond
            Algorithm = record[5]
            requests = record[6:]
            print(f'{DS_NO:<8}{X:<7}{Y:<7}{Dir:<7}{Z:<5}{Algorithm:<12}',requests)
            print("\nDisk Scheduling solution:\n")

            if (Algorithm == "Scan"):
                Scan(record)
            elif (Algorithm == "C - Scan"):
                C_Scan(record)
            elif (Algorithm == "C - look"):
                C_Look(record)
            elif (Algorithm == "Look"):
                Look(record)
            else:
                print("wrong algorithm")

start()