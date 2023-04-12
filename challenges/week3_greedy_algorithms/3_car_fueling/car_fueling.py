def compute_min_refills(distance ,max_run, gas_stations):


    stops = 0 # gas station stops 
    last_stop_value = 0
    index = 0
    gas_stations.append(distance)



    while index < len(gas_stations):
        if gas_stations[index] - last_stop_value <= max_run:
            index += 1
            continue
        elif gas_stations[index] - gas_stations[index-1] > max_run or index == 0:
            return -1
        else:
             last_stop_value = gas_stations[index-1]
             stops += 1
    return stops



if __name__ == '__main__':

   d = int(input()) #distance between cities
   m = int(input()) # how much can the car drive in a full tank
   _ = int(input()) # number of stops 

   stops = list(map(int,input().split()))
   print(compute_min_refills(d, m, stops))
