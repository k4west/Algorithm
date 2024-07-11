s=input()
t=s[:8]
i=0
while ''.join(map(lambda x: chr(ord(x)^i), t))!='CHICKENS':i+=1
print(''.join(map(lambda x: chr(ord(x)^i), s)))