import string

class abc:
  
  def max:

    fin = open("Book1.txt","r")
    fin1 = fin.read()
    #print(fin1)
    #print("jhzxgjhxgc")

    fin2=fin1.split()
    max_A = max(fin2)
    print(max_A)
 
    
    fin3 = open("Book2.txt","r")
    fin4 = fin3.read()
    fin5 = fin4.split()
    max_B = max(fin5)
    print(max_B)

    

    fin6 = open("Book3.txt","r")
    fin7 = fin6.read()
    fin8 = fin7.split()
    max_C = max(fin8)
    print(max_C)

  def biggest:
    if len(max_A) > len(max_B):
      if len(max_A) > len(max_C):
        print("Biggest word in three books is : ", max_A)
      else:
        print("Biggest word in three books is : ", max_C)

    else:
      if len(max_B) > len(max_C):
        print("Biggest word in three books is: ", max_B)
      else:
        print("Biggest word in three books is: ", max_C)


obj1 = abc()
obj1.max()
obj1.biggest()
