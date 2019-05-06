ipAddress = input("Enter an IP address: ")
segment = 1
count = 0

if ipAddress:
    for i in range(0, len(ipAddress)):
        if ipAddress[i] in "0123456789":
            count += 1
            if i == (len(ipAddress) - 1) and ipAddress[i] != '.':
                print("Segment {0} contains {1} numbers".format(segment, count))
        else:
            print("Segment {0} contains {1} numbers".format(segment, count))
            segment += 1
            count = 0
else:
    print("IP Address is empty!")
