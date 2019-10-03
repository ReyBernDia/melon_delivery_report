#     #print day of respective file 
# print("Day 1")
# #open file for Day 1 
# the_file = open("um-deliveries-20140519.txt")
# #iterate through lines in opened file 
# for line in the_file:
#     #strip out /n lines in file 
#     line = line.rstrip()
#     #creat list of [Melon Name, Count Sold, Total Amount Sold in $]
#     words = line.split('|')
#     #variable for each item in "words" called by index
#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     #print out report for CEO calling variables melon, count, amount
#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# #close opened file     
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


def open_delivery_files(desired_file):
    """Open file and return melon name, count, amount dollar worth"""
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
    return "End of the summary for this day."
    #close opened file     
    the_file.close()


print("Day 1")
day_1 = open_delivery_files("um-deliveries-20140519.txt")
print(day_1)

print("Day 2")
day_2 = open_delivery_files("um-deliveries-20140520.txt")
print(day_2)

print("Day 3")
day_3 = open_delivery_files("um-deliveries-20140521.txt")
print(day_3)




