bin_dic = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "0101", 6: "0110", 7: "0111",
           8: "1000", 9: "1001"}

char = input("Enter a character: ")

num_list = []

i = 0
for digit in str(ord(char)):
    num_list.insert(i, int(digit))
    i += 1

bcd_list = []

i = 0
for digit in num_list:
    bcd_list.insert(i, bin_dic[digit])
    i += 1

print("".join(map(str, bcd_list)))
