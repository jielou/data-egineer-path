
# SettingWithCopy Warning

## Intro



## settingwithwarning

```python
mask = df.z==0
df[mask]["z"]=0
## got warning
```

### why got warning?
you are trying to modify the copy of a dataframe. `df[mask]` gives the copy of df.

### how to avoid warning?
- Avoid chained assignments that combine two or more indexing operations like `df["z"][mask] = 0` and `df.loc[mask]["z"] = 0`.
- Apply single assignments with just one indexing operation like `df.loc[mask, "z"] = 0`. This might (or might not) involve the use of accessors, but they are certainly very useful and are often preferable.

## view and copies in Numpy and Pandas

```python
arr = np.array([1,2,4,8,16,32])
arr[1:4:2] # array([2,8]) shallow copy
arr[1:4:2].base # array([1,2,4,8,16,32])
arr[1:4:2].flags.owndata # False

arr[[1,3]] # array([2,8]) deep copy
arr[[1,3]].base # array([1,2,4,8,16,32])
arr[[1,3]].flags.owndata # True
```

### views in numpy

A shallow copy or view is a NumPy array that doesn’t have its own data. It looks at, or “views,” the data contained in the original array. You can create a view of an array with `.view()`. `.view()` is a view, or shallow copy, of the original array arr. The attribute .base of view_of_arr is arr itself. In other words, view_of_arr doesn’t own any data—it uses the data that belongs to arr. 

``` python
view_of_arr = arr.view() # array([ 1,  2,  4,  8, 16, 32])
view_of_arr.base # array([ 1,  2,  4,  8, 16, 32])
view_of_arr.base is arr # True
view_of_arr.flags.owndata # False
```

### copies in Numpy

A deep copy of a NumPy array, sometimes called just a copy, is a separate NumPy array that has its own data. The data of a deep copy is obtained by copying the elements of the original array into the new array. The original and the copy are two separate instances. You can create a copy of an array with `.copy()`

```python
copy_of_arr = arr.copy()
copy_of_arr # array([ 1,  2,  4,  8, 16, 32])
copy_of_arr.base is None # True
copy_of_arr.flags.owndata # True
```

### differences between views and copies in numpy
- Views don’t need additional storage for data, but copies do.
- Modifying the original array affects its views, and vice versa. However, modifying the original array will not affect its copy.

### views and copies in Pandas
```python
view_of_df = df.copy(deep=False)
copy_of_df = df.copy()

# numpy representations differences
view_of_df.to_numpy().base is df.to_numpy().base # True
copy_of_df.to_numpy().base is df.to_numpy().base # False

```


df and view_of_df share the same row and column labels, while copy_of_df has separate index instances. Keep in mind that you can’t modify particular elements of `.index` and `.columns`. They are immutable objects.

### indices and clices in Numpy and Pandas

NumPy arrays and Pandas objects (DataFrame and Series) implement special methods that enable referencing, assigning, and deleting values in a style similar to that of containers:

- .`__getitem__()` references values.
- .`__setitem__()` assigns values.
- .`__delitem__()` deletes values.

When you’re referencing, assigning, or deleting data in Python container-like objects, you often call these methods:

- var = obj[key] is equivalent to `var = obj.__getitem__(key)`.
- obj[key] = value is equivalent to `obj.__setitem__(key, value)`.
- del obj[key] is equivalent to `obj.__delitem__(key)`.

#### numpy

Whether you get views or copies of the original data depends on the approach you use to index your arrays: slicing, integer indexing, or Boolean indexing.

```python
# views
#  Both a and b use arr as their bases and neither has its own data.
a = arr[1:3]
b = arr[1:4:2]
# copies
# arr and c are independent
c = arr[[1, 3]]
# mask: get a copy of the original array that contains only the elements that correspond to the True values of the mask
mask = [False, True, False, True, False, False]
d = arr[mask]
```
- Slicing arrays returns views.
- Using index and mask arrays returns copies.

```python
# chained indexing
# views
arr = np.array([1, 2, 4, 8, 16, 32])
arr[1:4:2][0] = 64
arr #array([ 1, 64,  4,  8, 16, 32])

# copies
arr = np.array([1, 2, 4, 8, 16, 32])
arr[[1, 3]][0] = 64
arr # array([ 1,  2,  4,  8, 16, 32])
```

#### pandas 

```python
df["a":"c"] # a view
df[["a","b","c"]] # a copy
df[mask] # a copy
df[mask]["z"]=0 # settingwithcopy warning
df["z"][mask] # ok evaluation order matters
df.loc[mask] # return a copy
df.loc[["a", "c", "e"]]["z"] = 0  # Assignment fails, no warning
df[:3]["z"] = 0  # Assignment succeeds, with warning
df.loc["a":"c"]["z"] = 0  # Assignment succeeds, with warning
```

The recommended way of performing such operations is to avoid chained indexing. Like `df.loc[mask, "z"] = 0`.

In Pandas, the difference between creating views and creating copies also depends on the data types used.

### change the default settingwithcopywarning behavior

To change this behavior, you can modify the Pandas mode.chained_assignment option with pandas.set_option(). You can use the following settings:

- pd.set_option("mode.chained_assignment", "raise") raises a SettingWithCopyException.
- pd.set_option("mode.chained_assignment", "warn") issues a SettingWithCopyWarning. This is the default behavior.
- pd.set_option("mode.chained_assignment", None) suppresses both the warning and the error.