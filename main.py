'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if (n==0 or n==1):
    return False
  for d in range (2, n//2):
    if (n%d==0):
      return False
  return True

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for el in range (0,len(lst)):
    prod = prod* lst[el]
  return prod
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while (x!=y): 
   if(x>y):
    x=x-y;
   else:
    y=y-x;
  return x       
   
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  while(x != 0):
      r = y % x;
      y = x;
      x = r;
  return y
  
def main():
  # interfata de tip consola aici
  print ('''
     1. Is prime
     2. Product
     3. Cmmdc v1
     4. Cmmdc v2
  ''')
  x= int (input("Comanda:"))
  if (x==1):
    #is prime
    n= int (input("Introduceti n="))
    print (is_prime(n))
  if (x==2):
    #product
    n= int (input("Introduceti n="))
    list = []
    for i in range (0,n):
      el=int(input())
      list.append(el)
    print('produs=',get_product(list))
  if (x==3):
    #cmmdc v1
    x= int (input("Introduceti x="))
    y= int (input("Introduceti y="))
    print('cmmdc=',get_cmmdc_v1(x,y))
  if (x==4):
    #cmmdc v2
    x= int (input("Introduceti x="))
    y= int (input("Introduceti y="))
    print('cmmdc=',get_cmmdc_v2(x,y))
    
  
      

if __name__ == '__main__':
  main()
