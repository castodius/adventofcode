import sys

sensors = {}
beacons = set()

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

  sensors[sensor] = calculate_distance(sensor)(beacon)
  beacons.add(beacon)
    
def in_range(x, y):
  if (x, y) in beacons:
    return True
  get_distance_from_point = calculate_distance((x, y))
  for sensor in sensors:
    distance = sensors[sensor]
    if get_distance_from_point(sensor) <= distance:
      return True

  return False

def solve():
  points = []
  total_x = 0
  total_y= 0
  for sensor in sensors:
    out_of_range = sensors[sensor] + 1
    sensor_x, sensor_y = sensor

    x = sensor_x - out_of_range
    y = sensor_y
  
    # ladder NE
    while y < sensor_y + out_of_range:
      if not in_range(x, y):
        points.append((x, y))
        total_x+=x
        total_y+=y
      x += 1
      y += 1

    # ladder SE
    while y > sensor_y:
      if not in_range(x, y):
        points.append((x, y))
        total_x+=x
        total_y+=y
      x += 1
      y -= 1
    
    # ladder SW
    while y > sensor_y - out_of_range:
      if not in_range(x, y):
        points.append((x, y))
        total_x+=x
        total_y+=y
      x -= 1
      y -= 1

    # ladder NW
    while y < sensor_y:
      if not in_range(x, y):
        points.append((x, y))
        total_x+=x
        total_y+=y
      x -= 1
      y += 1

  average_x = total_x//len(points)
  average_y = total_y//len(points)

  best = 10**8
  best_point = (1,1)
  dist_function = calculate_distance((average_x, average_y))
  for point in points:
    distance = dist_function(point)
    if distance < best:
      best = distance
      best_point = point
  
  return best_point[0]*4*10**6 + best_point[1]

print(solve())
