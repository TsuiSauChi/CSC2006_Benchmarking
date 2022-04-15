import json
import requests
import time

### Define HTTP EndPoint
Application = "testsauchi"
APIKey = "NNSXS.VHLPH6BUMFKLCBTGAGEWXGPHJBH5YOWQ3OMAJ5Q.FBLAYZHHKTNU37QLAD3QWH4TBQ3OOOYQUAM3HSRLW5RYMT6A3EDA"
NumberOfRecords = 1
URL = "https://au1.cloud.thethings.network/api/v3/as/applications/" + Application + "/packages/storage/uplink_message?order=-received_at&limit=" + str(NumberOfRecords)
Header = { "Accept": "text/event-stream", "Authorization": "Bearer " + APIKey }

print("\n\nFetching from data storage...\n")

def Average(lst):
    return sum(lst) / len(lst)


time_list = []

# Loop 50 times and calculate the average
for i in range(100):
    print("COUNTER: ", i)
    start_time = time.time()
    r = requests.get(URL, headers = Header)
    time_list.append(time.time() - start_time)

average = Average(time_list)
  
# Printing average of the list
print("Average of the list =", average)

print("Response: {}\n".format(r.text))
print()