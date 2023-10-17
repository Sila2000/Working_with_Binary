#author Sila2000
def carry_bit_add(bit1, bit2):
    if bit1 == bit2 == '0':
        return '0'
    elif bit1 == '0' and bit2 == '1':
        return '0'
    elif bit1 == '1' and bit2 == '0':
        return '0'
    elif bit1 == '1' and bit2 == '1':
        return '1'


def sum_bit_add(bit1, bit2):
    if bit1 == bit2 == '0':
        return '0'
    elif bit1 == '0' and bit2 == '1':
        return '1'
    elif bit1 == '1' and bit2 == '0':
        return '1'
    elif bit1 == '1' and bit2 == '1':
        return '0'


def bin_extender(bin1, bin2):
    bin1_list = list(map(str, bin1))
    bin2_list = list(map(str, bin2))

    if len(bin1_list) >= len(bin2_list):
        bin1_list.insert(0, '0')
        bin2_list = ['0'] * (len(bin1_list) - len(bin2_list)) + bin2_list
        return bin1_list, bin2_list
    else:
        bin2_list.insert(0, '0')
        bin1_list = ['0'] * (len(bin2_list) - len(bin1_list)) + bin1_list
        return bin1_list, bin2_list


result = []


def bin_adder(bin1, bin2):
    bin_set = bin_extender(bin1, bin2)
    bin1_list = bin_set[0]
    bin2_list = bin_set[1]

    carry_bits = []
    sum_bits = []
    #after using bin_extender function upon bin1 and bin2, bin1_list and bin2_list are of same length
    for i in range(len(bin1_list)):
        carry_bits.append(carry_bit_add(bin1_list[i], bin2_list[i]))
        sum_bits.append(sum_bit_add(bin1_list[i], bin2_list[i]))

    result.insert(0, sum_bits[len(sum_bits) - 1])
    sum_bits.pop(len(sum_bits) - 1)

    #check whether all elements of sum_bits and carry_bits are zero or not
    count_sum_zero = 0
    count_carry_zero = 0

    for i in range(len(sum_bits)):
        if sum_bits[i] == '0':
            count_sum_zero += 1
    for i in range(len(carry_bits)):
        if carry_bits[i] == '0':
            count_carry_zero += 1

    if count_carry_zero == len(carry_bits) and count_sum_zero == len(sum_bits):
        return ''.join(map(str, result))
    else:
        bin1 = ''.join(map(str, sum_bits))
        bin2 = ''.join(map(str, carry_bits))
        return bin_adder(bin1, bin2)


print("Binary addition (Only Integral):")
bit_num1 = str(input("Enter the 1st binary number: "))
bit_num2 = str(input("Enter the 2nd binary number: "))

print(f"{bit_num1} + {bit_num2} = ", bin_adder(bit_num1, bit_num2))
