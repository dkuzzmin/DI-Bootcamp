#2 Exercise 2: Working With JSON

import json

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)

salary = data['company']['employee']['payable']['salary']

print(salary)

data['company']['employee']['birth_date'] = ''  


with open(dir_path + "//sampleJson.json", 'w') as f:
    json.dump(data, f, indent=2)

