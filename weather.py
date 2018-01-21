"""
Weather forecasting for Paris, France.
"""

class Weather(object):

    def condition(self):
        """Returns current weather condition."""
        if self.is_rainy():
            return "☂︎ It’s rainy in Paris."

        raise Exception("What? Not raining? Ok, that’s an exception.")

    def forecast(self, date):
        """Returns a weather forecast for the specified date."""
        if self.is_rainy(date):
            return "☂︎ It will rain in Paris."

        raise Exception("What? no rain? Ok, there is something wrong.")


    def is_rainy(self, date=None):
        return True
