import sys

Y = 2*10**6

sensors = {}
beacons = set()
start_x = 0

min_x = 10**7
max_x = 0

def calculate_distance(point1):
  return lambda x: abs(point1[0]-x[0]) + abs(point1[1]-x[1])

for line in sys.stdin:
  data = line.strip().split(' ')
  
  sensor_x = int(data[2].rstrip(',').split('=')[1])
  sensor_y = int(data[3].rstrip(':').split('=')[1])
  sensor = (sensor_x, sensor_y)

  beacon_x = int(data[-2].rstrip(',').split('=')[1])
  beacon_y = int(data[-1].split('=')[1])
  beacon = (beacon_x, beacon_y)

  min_x = min(min_x, sensor_x)
  max_x = max(max_x, sensor_x)

  sensors[sensor] = calculate_distance(sensor)(beacon)
  beacons.add(beacon)
    
def in_range(x, y = Y):
  get_distance_from_point = calculate_distance((x, y))
  for sensor in sensors:
    distance = sensors[sensor]
    if get_distance_from_point(sensor) <= distance:
      return True

  return False

points = 0
for x in range(min_x - 10 ** 6, max_x + 10 ** 6):
  if (x, Y) in beacons:
    continue
  if in_range(x):
    points += 1

print(points)
