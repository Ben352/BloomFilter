# Bloomfilter

A Python based Bloom filter. This probabilistic data structure is able to quickly verify set membership with a low false positive rate and a zero False negative rate. Such a strcuture is helpful when speed is valued more than a small false positive rate. For example in the context of databases and indexing. A Bloom filter can safely say when a key is not in a db and thus prevent a lookup. A false positive in this context would cause the db to perform an unnecessary lookup which is a good tradeoff in most cases.

# Usage
```python
bloom = BloomFilter()
filterSize = bloom.calcFilterLenght(1000,0.01)
k = bloom.calcKHashFuncs(filterSize,1000)
bloom.insert("Hello")
bloom.search("Hello") -> True
bloom.search("World") -> False
```

# TODO
- Dynamically generate hash functions using a salt (6 hashfunctions currently)
- Visualize the calculations for the filter size and the amount of hash functions using plots
