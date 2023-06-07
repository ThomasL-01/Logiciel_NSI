import time
a=0
b=0
while True:
 a+=1
 time.sleep(0.9)
 if a==60:
  a=0
  b=1
 print(b,"min",a,"sec")
 
