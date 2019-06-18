

def is_harshard(num):
    sum_of_numbers = 0
    dup = num 
    while(num > 0):
        digit = num % 10
        sum_of_numbers += digit
        num = num // 10

    if( (dup % (sum_of_numbers)) == 0):
        print(True)
    else :
        print(False)

print('enter the number')
num = int(input())

is_harshard(num)