#author Sila2000
# Convert decimal into binary

import math

d_num = original_num = int(input("Enter a decimal number: "))

if d_num == 0 or d_num == 1:
    print(f"Binary of {d_num} =", d_num)

elif d_num > 1:
    loop_factor = math.floor(math.log(d_num, 2)) + 1
    bin_sum = 0
    for i in range(loop_factor):
        boss = math.floor(math.log(d_num, 2))
        bin_sum += pow(10, boss)
        d_num -= pow(2, boss)
        if d_num == 0:
            break
    print(f"Binary of {original_num} =", bin_sum)

else:
    d_num = abs(d_num)
    loop_factor = math.floor(math.log(d_num, 2)) + 1
    bin_sum = 0
    for i in range(loop_factor):
        boss = math.floor(math.log(d_num, 2))
        bin_sum += pow(10, boss)
        d_num -= pow(2, boss)
        if d_num == 0:
            break
    bin_list = []

    AnsToQues = int(input("In 1's complement or 2's complement (Press 1 or 2): "))
    if AnsToQues == 1:
        i = 0
        while bin_sum != 0:
            rem = bin_sum % 10
            bin_list.insert(i, rem)
            bin_sum //= 10
            i += 1
        bin_list.append(0)
        bin_list.reverse()
        #print(bin_list)

        for index in range(len(bin_list)):
            if bin_list[index] == 1:
                bin_list.pop(index)
                bin_list.insert(index, 0)

            elif bin_list[index] == 0:
                bin_list.pop(index)
                bin_list.insert(index, 1)
        #print(bin_list)
        print(f"1's complement of {original_num} =", ''.join(map(str, bin_list)))
        #-> 1s complement

    #for 2s complement
    elif AnsToQues == 2:
        bit_count = 0
        while bin_sum != 0:
            rem = bin_sum % 10
            bin_sum //= 10
            bit_count += 1
        bit_count += 1
        #print(bit_count)
        d_num = pow(2, bit_count) + original_num
        #print(d_num)

        #conversion of d_num will give us the 2s complement of original_num
        loop_factor = math.floor(math.log(d_num, 2)) + 1
        bin_sum = 0
        for i in range(loop_factor):
            boss = math.floor(math.log(d_num, 2))
            bin_sum += pow(10, boss)
            d_num -= pow(2, boss)
            if d_num == 0:
                break
        print(f'2s complement of {original_num}=', bin_sum)
