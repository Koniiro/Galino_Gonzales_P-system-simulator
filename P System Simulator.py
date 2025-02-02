time=0
valid_rl=[]
import json
import random
# Open and read the JSON file
with open('sm_test.json', 'r') as file:
    data = json.load(file)



def rule_printer(rule):
    print("===Apply Rule===")
    print("Type: "+ rule["type"])
    print("Input: " + ", ".join(f"{obj['type']}^{obj['count']}" for obj in rule["input"]), end=" ; ")
    print("Output:" +", ".join(f"{obj['type']}^{obj['count']} " for obj in rule["output"]))
    



while(time !=5):
    #determine which rules may be used
    print(f"===Time: {time} ===" )
    for memb in data["membranes"]: # loop through all membranes
        if memb["objects"]==[]: #if no children. no need to apply rules
            continue
        object_dict = {obj["type"]: obj["count"] for obj in memb["objects"]}
        to_add = {obj["type"]: 0 for obj in memb["objects"]}
        for i_r in memb["rules"]: #checks which rules may be applied this round
            
            for i_r1 in i_r["input"]:
                if i_r1["type"] not in object_dict or i_r1["count"] > object_dict[i_r1["type"]]:
                    continue
            valid_rl.append(i_r)
  
        while(len(valid_rl)!=0): #loop until all rules are no longer usable
            gacha=random.randint(0, len(valid_rl) - 1)
            unusable=False	#change to True if rule can no longer be used for popping
            app_rl=valid_rl[gacha]
            
            object_dict = {obj["type"]: obj["count"] for obj in memb["objects"]}
            
            #test if rule can be applied
            for i_r1 in app_rl["input"]:	#loop through input reqs
                if i_r1["type"] not in object_dict or i_r1["count"] > object_dict[i_r1["type"]]:
                    unusable=True
                    break
            
            if unusable == False:

                rule_printer(app_rl)
                #print(i["objects"])
                
                # process inputs
                for obj_int in app_rl["input"]:
                    for obj in memb["objects"]:
                        if obj["type"]==obj_int["type"]:
                           obj["count"]-= obj_int["count"]
                           break
                #print(i["objects"])
                
                #add to temporary inputs
                for obj_out in app_rl["output"]:
                    if obj_out["type"] in to_add: #case where object already exists
                        to_add[obj_out["type"]]+=obj_out["count"]
                    else:
                        to_add[obj_out["type"]]=obj_out["count"]
 
                
            else:
                valid_rl.pop(gacha) #pop rule if no longer able to apply
                
               
       #print(memb["objects"])
        #print(to_add)
        
        #apply new objects
        target = {obj["type"]: obj for obj in memb["objects"]}  
        for i in to_add:
            if i in target:
                target[i]["count"] += to_add[i]
            else:
       
                memb["objects"].append({"type":i,"count":to_add[i]})
        
        print(memb["objects"])
        
        app_rl=""
        valid_rl=[]
        
    
        
        
        
    time+=1
   
        
                
            
        



    
  
