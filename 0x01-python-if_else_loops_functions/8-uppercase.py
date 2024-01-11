str = "albert"
def uppercase(str):
    str = "albert"
     for i in str:
         if ord(i) >= 'a' and ord(i) <= 'z':
             i = chr(ord(i) - 32)
         print("{}".format(i), end = "")

