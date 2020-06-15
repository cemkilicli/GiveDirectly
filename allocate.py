

target_distribution_list = {'Kenya UBI' : 0.33, 'Kenya Standard' : 0.33, 'Uganda Refugees' : 0.33 }

donations_list = { "Joe" : "", "Piali" : "", "Katie" : "Kenya Standard", "Isobel" : "" , "Mitch" : "" , "Eric" : "", "Jeff" : "Uganda Refugees", "Madeleine" : "", "Meylakh" : "Uganda Refugees", "Maya" : ""}


# --------- #
# VERSION 1 #
# --------- #

def alocate_funds_v1 (target_distribution, donations):

    allocation_list = donations
    counter_dict = dict()
    comp = list()
    stepper = 1/len(donations)

    # setting up counters
    for key in target_distribution.keys():

        counter_dict[key]=0
        comp.append(target_distribution[key])

    #finding already alocated funds
    for donation in donations:

        for key in  counter_dict.keys():
            
            if key == donations[donation]:

                counter_dict[key] = counter_dict[key] + stepper


    #making remaining allocations
    #evely distributing allocations
    for key in counter_dict:

        for donation in donations:

            if donations[donation] == "":
                
                if counter_dict[key] + stepper > target_distribution[key]:
                    break

                if counter_dict[key] < target_distribution[key]:

                    allocation_list[donation] = key
                    counter_dict[key] = counter_dict[key] + stepper

    #adding remaining allocations
    for key in counter_dict:

        for donation in donations:
         
            if donations_list[donation] == "":
                
                if counter_dict[key] < target_distribution[key]:

                    allocation_list[donation] = key
                    counter_dict[key] = counter_dict[key] + stepper

    print("Allocation Counts:")
    print("------------------")
    for key in counter_dict:
        print(key,":",sum(map((key).__eq__, allocation_list.values())))

    print("----------------")
    print("Allocation list:")
    print("----------------")
    print(allocation_list) 
     

    return allocation_list



#alocate_funds_v1(target_distribution_list,donations_list)

# --------- #
# VERSION 2 #
# --------- #

# user preferances is a dictionary which matches user with their prefered projects 
user_preferance_list = { "Joe" : "", "Piali" : "", "Katie" : "Kenya UBI", "Isobel" : "" , "Mitch" : "" , "Eric" : "Kenya Standard", "Jeff" : "Kenya Standard", "Madeleine" : "Kenya Standard", "Meylakh" : "", "Maya" : ""}

# This algorithm will unballance the ratios that are given in target_distribution_list 
# if the users decides to favor the projects in an un-ballanced manner
# This agorithm does not re-allocate donations if they are already allocated.

def alocate_funds_v2 (target_distribution, user_preferances, donations):
    
    allocation_list = donations

    for donation in donations:

        for user_preferance in user_preferances:

            if user_preferance == donation:

                if user_preferances[user_preferance] != "":  
                
                    if donations[donation] == "":

                        donations[donation] = user_preferances[user_preferance]

                    elif donations[donation] != user_preferances[user_preferance]:
                        print("------------------")
                        print("WARNING: System can not allocate ",donation,
                        "'s donation to",user_preferances[user_preferance],
                        "project.", "The donation is already allocated to", donations[donation],
                        "project.")
                        

    alocate_funds_v1(target_distribution, donations)

    return allocation_list


alocate_funds_v2(target_distribution_list,user_preferance_list,donations_list)