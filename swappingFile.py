def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
        dataA = a.read()
      
    with open(file2, 'r') as b:
        dataB = b.read()
    
    with open(file1, 'w') as a:
        a.write(dataB)

    with open(file2, 'w') as b:
        b.write(dataA)

swapFileData()
