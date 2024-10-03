import os
import time
while(True):
    #Primero
    os.system ("cls")
    print ("")  
    for i in range (9):
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    for i in range (7,-1,-1):
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    #time.sleep(0.5)
    os.system ("cls")

  
    #Tercero
    print ("")   
    for i in range (9):
        print (" "*i, end="")
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    for i in range (7,-1,-1):
        print (" "*i, end="")
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    #time.sleep(0.5)
    os.system ("cls")

      #Segundo
    print ("")   
    for i in range (9):
        print ("  "*i, end="")
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    for i in range (7,-1,-1):
        print ("  "*i, end="")
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    #time.sleep(0.5)
    os.system ("cls")

    #Cuarto
    print ("")   
    for i in range (9):
        print (" "*i, end="")
        for j in range (i, 9):
            print (j, end= " ")
        print ("")
    for i in range (7,-1,-1):
        print (" "*i, end="")
        for j in range (8,i-1,-1):
            print (j, end= " ")
        print ("")
    #time.sleep(0.5)
    os.system ("cls")