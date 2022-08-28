i=1
mensaje=""
while i<=100:
    if i % 3 == 0:
        mensaje="fizz"
    elif i % 5 == 0:
        mensaje="buzz"
    else:
        mensaje=i

    if i % 3 == 0 and i % 5 ==0:
        mensaje="fizzbuzz"
    
    print(mensaje)
    
    i+=1
