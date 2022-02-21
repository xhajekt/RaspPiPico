# user_name = input("whats your name?")
# 
# if user_name == "Clark Kent":
#     print("You are superman!")
# else:
#     print("you are not superman :(")
    
    
import utime

number = int(input("how many times to repeat?"))
while True:
    utime.sleep(0.5)
    print(number)
    number=number-1
    if(number == 0):
        break
print("loop finished")