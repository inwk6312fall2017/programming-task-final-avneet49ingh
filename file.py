from weather import Weather

class temp:
  weather = Weather()
  
  def find_weather(self):
    data = weather.lookup_by_location('Halifax')
    condition = data.condition()
    print(condition['text'])

    for forecasts in location.forecasts():
      print(forecats['text'])
      print(forecats['date'])
      print(forecasts['high'])
      print(forecasts['low'])

  def max_temp():
    for i in forecasts['high']:
      if i > i+1:
        return i 
      else:
        return i+1

  def min_temp():
    for j in forecasts['low']:
      if j > j+1:
        return j+1 
      else:
        return j

  def rain():
    for k in forecasts['text']:
      if k == 'rain':
         print(forecasts['date']) 
      
