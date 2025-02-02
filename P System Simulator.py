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
            
            for i_r1 in i_r["input"]:
                if i_r1["type"] not in object_dict or i_r1["count"] > object_dict[i_r1["type"]]:
                    continue
            valid_rl.append(i_r)
  
        while(len(valid_rl)!=0): #loop until all rules are no longer usable
            gacha=random.randint(0, len(valid_rl) - 1)
            unusable=False	#change to True if rule can no longer be used for popping
            app_rl=valid_rl[gacha]
            
            object_dict = {obj["type"]: obj["count"] for obj in i["objects"]}
            
            #test if rule can be applied
            for i_r1 in app_rl["input"]:	#loop through input reqs
                if i_r1["type"] not in object_dict or i_r1["count"] > object_dict[i_r1["type"]]:
                    unusable=True
                    break
            
            if unusable == False:
                print("Apply" +str(app_rl))
                print(i["objects"])
                for obj_int in app_rl["input"]:
                    for obj in i["objects"]:
                        if obj["type"]==obj_int["type"]:
                           obj["count"]-= obj_int["count"]
                           break
                print(i["objects"])     
 
                
            else:
                valid_rl.pop(gacha) #pop rule if no longer able to apply
                
                
        
        print(to_add)
        
        
        
        
        if valid_rl==[]:
            break
    
            
            
   
        
        
        
        
        
        time+=1
        app_rl=""
        valid_rl=[]
    break
        
                
            
        
   #break


    
  
