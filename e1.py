class ew1:
    weather_data={
        'toro': ['13','partly sunny','8km/h nw'],
        'mon': ['16','mostly sunny','22km/h w'],
        'vanc': ['18','thunder showers','10km/h ne'],
        'newyork': ['17','mostly cloud','5km/h se'],
        'mumbai': ['33', 'humid and foggy', '2km/h s']
    }
    def __int__(self, city):
        self.city = city
    def gettemp(self):
        return self.weather_data[self.city][0]
    def getWeatherConditions(self):
        return self.weather_data[self.city][1]
    def getWindspeed(self):
        return self.weather_data[self.city][2]
    def getcity(self):
        return self.city


if __name__ == "__main__": ee1 = ew1('mumbai')
                            wind_dir_str_len = 2
    if ee1.getWindspeed()[-2:-1] == '': wind_dir_str_len = 1
    print("the current temp in", ee1.getcity(), "is",
          ee1.gettemp(), "degrees celsius",
          "the weather conditions are",
          ee1.getWeatherConditions(),
          "and the wind is coming out of the",
          ee1.getWindspeed()[-(wind_dir_str_len):],
          "direction with a speed of",
          ee1.getWindspeed()
          [0:len(ee1.getWindspeed()) - (wind_dir_str_len)])