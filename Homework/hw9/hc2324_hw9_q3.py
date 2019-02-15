import math as r

class BinaryPositiveInteger:
     def __init__(self, num):
         binary = ''
         while num // 2 != 0:
             binary = str(num % 2) + binary
             num = num // 2
         self.num ="1"+binary

     def __add__(self, other):
        while len(self.num) != len(other.num):
            if len(self.num) > len(other.num):
                other.num = "0"+other.num
            else:
                self.num = "0"+self.num
        self.sum = ''
        add = 0
        for i in range(-1, -len(self.num)-1, -1):
            if self.num[i] == '0' and other.num[i] == '0':
                if add == 0:
                    self.sum = '0' + self.sum
                    add = 0
                else:
                    self.sum = '1' + self.sum
                    add = 0
            elif self.num[i] == '1' and other.num[i] == '0':
                if add == 0:
                    self.sum = '1' + self.sum
                    add = 0
                else:
                    self.sum = '0' + self.sum
                    add = 1
            elif self.num[i] == '0' and other.num[i] == '1':
                 if add == 0:
                    self.sum = '1' + self.sum
                    add = 0
                 else:
                    self.sum = '0' + self.sum
                    add = 1
            elif self.num[i] == '1' and other.num[i] == '1':
                 if add == 0:
                    self.sum = '0' + self.sum
                    add = 1
                 else:
                    self.sum = '1' + self.sum
                    add = 1
        if add == 1:
            return "0b1"+ self.sum
        else:
            return "0b"+self.sum

     def __lt__(self, other):
       greater = False
       index = 0
       while greater == False:
           if other.num[index] == '1' and self.num[index] == '0':
               greater = True
               return False
           elif other.num[index] == '0' and self.num[index] == '1':
               greater = True
               return True
           else:
               index+=1

     def is_power_of_2(self):
        count = 0
        for i in self.num:
            if i == "1":
                count +=1
        if count == 1:
            return True
        else:
            return False

     def largest_power_of_2(self):
         return 2**(len(self.num)-1)

     def __repr__(self):
         return "0b" + self.num



def main():
    n1 =  BinaryPositiveInteger(13)
    print(n1)
    n2 = BinaryPositiveInteger(25)
    print(n2)
    #print(n1.is_power_of_2())
    #print(n1.largest_power_of_2())
    #print(n1<n2)
    #print(n1+n2)

main()