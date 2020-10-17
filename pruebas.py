'''i = 1
e = 1
while i != 100 or e != 1:
    print(i)
    i += 2
print("Programa terminado")'''

'''def calculo(i=0):
    print("hola mundo", i)
    i += 1
    return(i)
  
i = 10  
i = calculo(i)

print(i)
'''
def calculo(i, d):
    print(i, "y", d)
    d+=3
    i+=1
    return (i, d)

i = 1    
for d in [0, 1, ]:
    for j in [0, 1]:
        i,d = calculo(i ,d)

        
    