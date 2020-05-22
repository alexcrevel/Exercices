
number = str(17.45989)
def tronquer(number):
    integ, rest = number.split(".")
    return ",".join([integ, rest[:3]])

print(tronquer(number))