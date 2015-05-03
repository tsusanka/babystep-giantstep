#
# MKY assigment 3 Babystep-Giantstep alg
# help functions
#

def power(num, power, mod):
    # Calculates $num^$power mod $mod
    if power == 0:
        return 1
    result = 1
    for i in range(power):
        result = (result * num) % mod
    return result


def mult(a, b, mod):
    a = a * b
    return a % mod

def add(a, b, mod):
    return (a + b) % mod;

def valueExists(needle, haystack):
    return [item for item in haystack if item[1] == needle]
