# Paris weather forecasts

A simple mathematical model to provide weather forecasts for Paris, France.
Accuracy is estimated to be 91% based on the latest measurements.


## Usage

```python
import datetime
from meteo.weather import Weather

w = Weather()

# Get the current condition
print(w.condition())

# Get the forecast for tomorrow
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
print(w.forecast(tomorrow))
```

## Contributions

Any contribution is welcome! ;)



---
*Made in a rainy day in Paris ☂︎*

