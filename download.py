import json
import subprocess     

with open("data.json") as data_file:
    data = json.load(data_file)
    
    for i in data['Dependencies']:

    	subprocess.call(['pip', 'install', i])
    	
