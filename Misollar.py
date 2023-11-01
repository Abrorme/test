
def Juft(a): 
    # bu sonlikni aniqlang uchun funksiya
    if a % 2 == 0:
        return True
    return False 


b = [2,3,4,20]

resalt = list(map(lambda a: a**3, b))

print(resalt)