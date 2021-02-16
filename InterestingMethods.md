# List of acquired Pythonic methods

## Replace integer using Numpy

Replace the column with 0 if the condition is met, otherwise 1

```Python
dataframe['overweight'] = np.where(dataframe['overweight'] < 25, 0, 1)
```
