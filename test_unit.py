from bloomfilter import BloomFilter
import pytest

def test_filterSize():
    bloom = BloomFilter()
    filterSize = bloom.calcFilterLenght(10000,0.01)
    print(filterSize)
    assert(filterSize==95851)
def test_KHashFuncs():
    bloom = BloomFilter()
    filterSize = bloom.calcFilterLenght(10000,0.01)
    k = bloom.calcKHashFuncs(filterSize,10000)
    assert(k==7)
def test_positive_retrival():
    bloom = BloomFilter()
    filterSize = bloom.calcFilterLenght(1000,0.01)
    k = bloom.calcKHashFuncs(filterSize,1000)
    for x in ["aa","bb","cc","dd","ee","ff"]:
        bloom.insert(x)
    for x in ["aa","bb","cc","dd","ee","ff"]:
        res = bloom.search(x)
        assert(res == True)
def test_negative_retrival():
    bloom = BloomFilter()
    filterSize = bloom.calcFilterLenght(1000,0.01)
    k = bloom.calcKHashFuncs(filterSize,1000)
    for x in ["aa","bb","cc","dd","ee","ff"]:
        bloom.insert(x)
    assert(bloom.search("z") == False)
    