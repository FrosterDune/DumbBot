from math import sqrt

def vypocet(a:float, b:float, c:float):

    try:
        D = b ** 2 - 4 * a * c
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        return str(f"x1 = {x1}\nx2 = {x2}")
    except ValueError:
        return str("rovnice nemá řešení prde")

class Commands:

    def vypis(cls, a, b, c):
        return vypocet(a=a, b=b, c=c)
