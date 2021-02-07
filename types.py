# Classes

class HashableSigned16BitCoordinatePair:
    def __init__(self, x:int, y:int):
        "When hashed, results in a 64-bit integer. X and Y values must be in range(-(2**16), 2**16)"

        x = int(x)
        y = int(y)

        # 2**16
        assert x >= -65536 
        assert x < 65536
        assert y >= -65536
        assert y < 65536

        print(x+2147483648)
        print(x+2147483648 << 16)
        print(y+2147483648)
        print((x+2147483648 << 16) + y+2147483648)

        self.__HASH = (x+2147483648 << 16) + y+2147483648
    
    def __hash__(self):
        return self.__HASH
