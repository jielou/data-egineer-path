# time series visualization

## key concepts

### moving averages
In the field of time series analysis, a moving average can be used for many different purposes:
- smoothing out short-term fluctuations
- removing outliers
- highlighting long-term trends or cycles

```python
df.rolling(window=window).mean()
```
### aggregate values of your time series
```python
df["date"] = pd.to_datetime(df["date"])
df.set_index("date")
df.groupby(df.index.month).mean()
```