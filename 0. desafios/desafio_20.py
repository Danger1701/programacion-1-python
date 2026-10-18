def desafio_20(nums):
    
    result = ""

    for num in nums:
        if type(num) == int and 0 <= num <= 127:
            result += chr(num)
    
    # retorno los valores resultantes
    return result

lista1 = [ 49, 50, 51, 52, 53, 54, 55, 56, 57, 48 ]
print(desafio_20(lista1))

lista2 = [ 70, 114, 97, 110, 99, 105, 115, 99, 111]
print(desafio_20(lista2))