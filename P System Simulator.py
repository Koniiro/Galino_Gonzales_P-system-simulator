time=0
valid_rl=[]
import json
import random
# Open and read the JSON file
with open('sm_test.json', 'r') as file:
    data = json.load(file)

# Print the data
#print(data)
#print(data["membranes"][0]["rules"])

#def rule_applicant():
    

while(True):
    #determine which rules may be used
    for i in data["membranes"]: # loop through all membranes
        if i["objects"]==[]: #if no children. no need to apply rules
            continue
        object_dict = {obj["type"]: obj["count"] for obj in i["objects"]}
        to_add = {obj["type"]: 0 for obj in i["objects"]}
        for i_r in i["rules"]: #checks which rules may be applied this round
            object_dict = {obj["type"]: obj["count"] for obj in i["objects"]}
            
            for i_r1 in i_r["input"]:
                if i_r1["type"] not in object_dict or i_r1["count"] > object_dict[i_r1["type"]]:
                    continue
            valid_rl.append(i_r)
  
        #while(True):
        app_rl=valid_rl[random.randint(0, len(valid_rl) - 1)]
        for i_r1 in app_rl["input"]:
            if i_r1["type"] not in object_dict or i_r1["count"] > object_dict[i_r1["type"]]:
                continue
                
        
        print(to_add)
        
        
        
        
        if valid_rl==[]:
            break
    
            
            
   
        
        
        
        
        
        time+=1
        app_rl=""
        valid_rl=[]
    break
        
                
            
        
   #break


    
  
