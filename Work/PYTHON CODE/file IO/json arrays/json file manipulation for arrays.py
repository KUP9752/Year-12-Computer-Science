##To read
import json
r = open('arrayin.json','rt')
data = json.load(r)
r.close()

print(data)

numbers = [0,2,4,6,8]
w = open('arrayout.json','wt')
json.dump(numbers,w)
w.close()
      
