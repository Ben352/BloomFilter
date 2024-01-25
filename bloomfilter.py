from math import log,ceil
from hashlib import md5,sha1,sha224,sha256,sha384,sha512

class BloomFilter():
    def __init__(self):
        self.filterSize=0
        self.filter = None
        self.FPrate = 0
        self.kHashFunctions = 0
        self.hashFunctions = [md5,sha1, sha224,sha256,sha384,sha512]
    def hashFunc(self,x,y):
        hasher = x()
        y = y.encode()
        hasher.update(y)
        return int(hasher.hexdigest(),16)
    def calcFilterLenght(self,n=10000,p=0.01):
        self.FPrate = p
        m = -n * log(p)/(log(2)**2)
        m = ceil(m)
        self.filterSize = m
        print("Filter size is set to " + str(m))
        self.filter = [0] * m
        return m
    def calcKHashFuncs(self,m,n):
        k = m/n*log(2)
        k = ceil(k)
        self.kHashFunctions  = k
        print("For the accepted FP rate of "+str(self.FPrate) +" "+ str(k)+ " hash functions are needed.")
        return k
    def insert(self,element):
        assert(type(element)==str)
        for x in self.hashFunctions[0:self.kHashFunctions]:
            y = self.hashFunc(x,element)%self.filterSize
            self.filter[y] = 1
    def search(self,element):
        assert(type(element)==str)
        for x in self.hashFunctions[0:self.kHashFunctions]:
            y = self.hashFunc(x,element)%self.filterSize
            if self.filter[y] == 0:
                return False
        return True
    def __str__(self) -> str:
        return str(self.filter)