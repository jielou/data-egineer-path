# time series

## Intro

resources: [datacamp time series analysis in python]()

## key concepts

### autocorrelation

correlation of a time series with a lagged copy of itself

for example:

- lag-one autocorrelation
- mean reversion 
- Negative autocorrelation
- momentum, or trend following - positive autocorrelation

In python: `df.column.autocorr()`

### white noise
 whilte noise is a series with:
 - constant mean
 - constant variance
 - zero autocorrelations at all lags

 sepcial case: if data has normal distribution, then Gaussian White Noise.

 in Python,

 ```pyton
import numpy as np
noise = np.random.normal(loc=0, scale=1, size=500)
 ```

### random walk

#### Yt=Yt-1 + et
- change in series is white noise
- cannot forecast a random walk

#### random walk with drift: Yt=u+Yt-1+et
- change in series is white noise with non-zero mean

#### regression test for random walk
- Yt=a+bYt-1+et
- Yt-Yt-1 = a + b Yt-1 +et
    - test Ha: b=0 (random walk)

#### in python
```python
from statsmodels.tas.stattools import adfuller
adfuller(x)
```

### stationarity
- Strong stationarity:  entire distribution of data is time-invariant
- weak stationarity: mean, variance and autocorrelation are time-invariant (i.e., for autocorrelation, corr(Xt, Xt-T) is only a function of T)
- non-stationary serires:
    - random walk
    - seasonality in series
    change in mean or standard deviation over time
- transform nonstationary series into stationary series
    - take first difference
    - log first, then take seasonal difference


### AR（1) Model

Rt = u + a Rt-1 + et (AR model of order 1)

For stationariry, -1 < a <1
Negative a: mean reversion
positive a: mementum
a = 0: white noice
a=1: random walk

### Higher order AR models
- AR2: Rt = u + a1Rt-1+a2Rt-2+et
- AR3: Rt = u+a1Rt-1+a2Rt-2+a3Rt-3+et

### simulating a time series

```python
# import the module for simulating data
from statsmodels.tsa.arima_process import ArmaProcess

# AR parameter = +0.9
ar1 = np.array([1, -0.9])
ma1 = np.array([1])
AR_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = AR_object1.generate_sample(nsample=1000)
```

### fit AR model
```python
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

# Fit an AR(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(1,0))
res = mod.fit()

# Print out summary information on the fit
print(res.summary())

# Print out the estimate for the constant and for phi
print("When the true phi=0.9, the estimate of phi (and the constant) are:")
print(res.params)
```

### identifying the order of an AR model

- the order of an AR model will usually be unknown
- two techiniques to determine order
    - partial autocorrelation function (PACF)
    - information criteria: adjusts goodness-of-fit for number of parameters
        - AIC (Akaike Information Criterion)
        - BIC (Bayesian Information Criterion)

# MA model

- MA model of order 1: R2 = u+et- a et-1
- Negative a: one-period mean reversion
- Positive a: one-period momentum
- Note: one-period autocorrelation is a/(1+a2), not a

## Higher Order MA models

- MA(2): Rt = u + et - a1 et-1 - a2 et-2
- MA(3): Rt = u + et - a1 et-1 - a2 et-2 - a3 et-3

### ARMA Model

- ARMA(1,1,): Rt = u + aRt-1 + et + b et-1

### converting between ARMA, AR and MA models
- converting AR(1) to an MA (infinity)

### Cointegration models

Two series Pt and Qt can be random walks, but the linear combination Pt-c Qt may not be a random walk. If that's true
- Pt - c Qt is forecastable
- Pt and Qt are cointegrated

#### Analogy: Dog on a leash
#### what types of series are cointegrated
- economic substitutes
- competitors

#### how to tet for cointegration
- regress Pt on Qt and get slope c
- Dickey-Fuller test on Pt - c Qt to test for random walk

