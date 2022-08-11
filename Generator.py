#ganerater password!

from ast import If
import random
sumM = 0
strEr = ""
#**************************************#
low_case = "abcdefghijklmnopqrstuvwxyz"
upp_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/\?"
#*************************************************#
user_for = low_case + upp_case + numbers + symbols
#*************************************************#
print("!!! ENTRY IS BY NUMBERS ONLY !!!")
#*************************************************#
lenght_for_pass = int(input("ENTRY IS BY NUMBERS ONLY: "))
password = "".join(random.sample(user_for, lenght_for_pass))
#************************************************************#

print("The password is: " + password)
print("By D.Dimov!!!")

