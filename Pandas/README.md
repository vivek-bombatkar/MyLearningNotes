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

### Change data type of columns

```python
b = [['a',10,100],['b',20,200]]
b_cols = ['c1','c2','c3']
df_b = pd.DataFrame(b,columns=b_cols)
print(df_b)
#apply
df_b[['c2','c3']] = df_b[['c2','c3']].apply(pd.to_numeric) 
print(df_b.dtypes)

#astype
df_b[['c2','c3']] = df_b[['c2','c3']].astype(float) 
print(df_b.dtypes)
```

      c1  c2   c3
    0  a  10  100
    1  b  20  200
    c1    object
    c2     int64
    c3     int64
    dtype: object
    c1     object
    c2    float64
    c3    float64
    dtype: object
    

```python
b = [['a',10,100.11],['b',20,200.22]]
b_cols = ['c1','c2','c3']
df_b = pd.DataFrame(b,columns=b_cols)
print(df_b)
#infer_objects
df_b = df_b.infer_objects()
df_b.dtypes
```

      c1  c2      c3
    0  a  10  100.11
    1  b  20  200.22
    

    c1     object
    c2      int64
    c3    float64
    dtype: object


### Delete column from pandas DataFrame



```python
import pandas as pd
import numpy as np
```


```python
df_a = pd.DataFrame({
    'b': np.random.choice([3,6,9,np.nan],5),
    'c': np.random.choice(['aa','bb','cc'],5)
})
df_a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9.0</td>
      <td>bb</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>bb</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>bb</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>aa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.0</td>
      <td>aa</td>
    </tr>
  </tbody>
</table>
</div>




```python
del df_a['b']
df_a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bb</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bb</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bb</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>aa</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_b = df_a.columns.drop('c',1)
df_b
```




    Index([], dtype='object')


