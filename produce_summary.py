def open_delivery_files(day_number, desired_file):
    """Given day number & delivery file, returns report"""

    print("-- Day ", day_number, "--")
    #open file for Day 1 
    the_file = open(desired_file)
    #iterate through lines in opened file 
    for line in the_file:
        #strip out /n lines in file 
        line = line.rstrip()
        #creat list of [Melon Name, Count Sold, Total Amount Sold in $]
        words = line.split('|')
        #variable for each item in "words" called by index
        melon = words[0]
        count = words[1]
        amount = words[2]

        #print out report for CEO calling variables melon, count, amount
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    return "-- End of the summary for this day. --"
    #close opened file     
    the_file.close()



day_1 = open_delivery_files(1, "um-deliveries-20140519.txt")
print(day_1)


day_2 = open_delivery_files(2, "um-deliveries-20140520.txt")
print(day_2)


day_3 = open_delivery_files(3, "um-deliveries-20140521.txt")
print(day_3)




