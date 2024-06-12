# Write your solution here
import math

def get_station_data(filename: str):
  data_list = {}
  with open(filename) as data_file:
    for data in data_file:
      data = data.replace("\n", "")
      line = data.split(";")
      if line[3] == "name":
        continue
      data_list[line[3]] = (float(line[0]), float(line[1]))
  return data_list



def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_as_km = (longitude1-longitude2) * 55.26
    y_as_km = (latitude1-latitude2) * 111.2
    return math.sqrt(x_as_km**2 + y_as_km**2)


def greatest_distance(stations: dict):
  station_name = []
  greatest = 0
  
  for station in stations:
    station_name.append(station)

  for i in range(len(station_name)):
    for j in range(i, len(station_name)-1):
      d = distance(stations, station_name[i], station_name[j+1])
      if d > greatest:
        greatest = d
        station1 = station_name[i]
        station2 = station_name[j+1]
  return station1, station2, greatest

      

if __name__ == "__main__":

  stations = get_station_data('stations1.csv')
  station1, station2, greatest = greatest_distance(stations)
  print(station1, station2, greatest)
