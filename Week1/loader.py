import json

data = '{"name": "Anass", "age": 20}'
parsed = json.loads(data)
print(parsed["name"])                
