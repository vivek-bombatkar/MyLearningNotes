# Pandas---My-learning-notes
Pandas---My-learning-notes

## Usefule links

http://pandas.pydata.org/pandas-docs/stable/10min.html

http://www.datasciencemadesimple.com/get-minimum-value-column-python-pandas/

https://github.com/IST256/learn-python/tree/master/content/lessons/12

https://stackoverflow.com/questions/tagged/pandas?sort=frequent&pageSize=15

http://seanlaw.github.io/2016/05/25/pandas-end-to-end-example/

https://github.com/GalvanizeOpenSource/live-coding-pandas-lda/blob/master/live_coding.ipynb

https://github.com/hyunhw/ml-pandas-examples/blob/master/Pandas/1_Pandas_basic.ipynb



## Notes:

### pandas iloc vs ix vs loc explanation, how are they different?
https://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation-how-are-they-different
```
First, here's a recap of the three methods:

loc gets rows (or columns) with particular labels from the index.
iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.
It's important to note some subtleties that can make ix slightly tricky to use:

if the index is of integer type, ix will only use label-based indexing and not fall back to position-based indexing. If the label is not in the index, an error is raised.

if the index does not contain only integers, then given an integer, ix will immediately use position-based indexing rather than label-based indexing. If however ix is given another type (e.g. a string), it can use label-based indexing.
```
