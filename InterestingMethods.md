# Python methods

## Replace integer using Numpy

Replace the column with 0 if the condition is met, otherwise 1

```Python
dataframe['overweight'] = np.where(dataframe['overweight'] < 25, 0, 1)
```
## Convert a Pandas Dataframe form Wide to Long.

This was very new to me when I started this projects two days ago.
What does it mean for a dataframe to be wide?
Well, it is the standard formate we are familiar with, see below.

![](https://i.imgur.com/Put7QZc.png)

However, to get a categorical plot with Seasborn's catplot() method, this structure must be converted to long format using the melt() method.

![](https://i.imgur.com/xDs3JhT.png)

### melt()

```python
data = datafram.melt(data, id_vars='', var_name='', value_name='')
```
Check the notebook for a use case of the method.
It basically shrinks/melt your data to a column with the variable names
and another with the corresponding values.

## Categorical plot with Catplot()

Seaborn's catplot() method accepts a long format and has different types of plots, check [here](https://seaborn.pydata.org/generated/seaborn.catplot.html) for the documentation.
Remember to use hue if you'd like to plot variables with multiple values.