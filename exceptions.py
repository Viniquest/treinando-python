try:
    result = 2 / 0
except ZeroDivisionError:
    print("não é possível dividir por zero!")
finally:
    result = 1

print (result) 

try:
    raise Exception("Um erro!")
except Exception as error:
    print(error)


# uso do with

#filename = '/Users/NGI/test.txt'

#with open(filename, "r") as file:
    #content = file.read()
    #print(content)