
def check_card_number(num):
 digits = [int(x) for x in reversed(str(num))]
 check_sum = sum(digits[::2]) + sum((dig//10 + dig%10) for dig in [2*el for el in digits[1::2]])
 return check_sum%10 == 0
  #if __name__ == "__main__":
  #print( check_card_number(input('')))

def atoi(s):
   s = s[::-1]
   num = 0
   for i, v in enumerate(s):
      for j in range(0, 10):
         if v == str(j):
            num += j * (10 ** i)
   return num

k='jianshe bank'
def generate_card_number(bank):
    bank = []
    if name == 'jianshe bank':
        for i in range(6227007201360049787, 6227007201360049987, 1):
            bank.append(i)
        return bank

a=atoi(k)
print(check_card_number(a))
