######################################################################
# Data Structures and Algorithms 2
# Kyle Hogue
# 000931190
######################################################################

from Package import Package
import My_Hash
import datetime

######################################################################
#
# Lists and variables to use later.
# 
######################################################################
# Lists for provided info
package_list = My_Hash.My_Hash() 
address_list = []
distance_list = []
# Punctuation so I can strip it from imported strings if needed.
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

######################################################################
#
# Read in Package Info, then builds and address list.
# 
######################################################################
# Opens file, reads in CSV, creates an object from each line, stores it in list, closes file.
f = open("WGUPS Package File.csv", "r")
for line in f:
    split_line = line.split(',')
    new_package = Package(int(split_line[0]), split_line[1], split_line[2], split_line[3], split_line[4], split_line[5],
                          int(split_line[6]), split_line[7].replace("\n", "*"), 'at the hub')
    My_Hash.My_Hash.my_hash_insert(package_list, new_package)
f.close()
# Opens file, reads a line, parses line, strips whitespace, checks is it begins with a number(ie. is an address), closes file.
a_list = []
f = open("WGUPS Distance Table.csv", "r")
for line in f:
    split_line = line.split(',')
    for string in split_line:
        new_string = string.strip()
        if new_string.startswith(tuple("123456789")):
            new_string = new_string.replace('"', "")
            a_list.append(new_string)               
f.close()
#strips duplicates from address_list
for line in a_list:
    if line not in address_list:
        address_list.append(line)

######################################################################
#
# Hard Coded Distance Table
#
# Spent time trying to clean csv reads, not worth when not required.
# 
###################################################################### 
distance_list.append([address_list[0], 0.0])
distance_list.append([address_list[1], 7.2, 0.0])
distance_list.append([address_list[2], 3.8, 7.1, 0.0])
distance_list.append([address_list[3], 11.0, 6.4, 9.2, 0.0])
distance_list.append([address_list[4], 2.2,	6.0, 4.4, 5.6, 0.0])
distance_list.append([address_list[5], 3.5,	4.8, 2.8, 6.9, 1.9, 0.0])
distance_list.append([address_list[6], 10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0])
distance_list.append([address_list[7], 8.6,	2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0])
distance_list.append([address_list[8], 7.6,	4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0])
distance_list.append([address_list[9], 2.8,	6.3, 1.6, 7.3, 2.6,	1.5, 8.0, 9.3, 4.8,	0.0])
distance_list.append([address_list[10], 6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0])
distance_list.append([address_list[11], 3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0])
distance_list.append([address_list[12], 7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2,	7.7, 0.6, 5.1, 12.0, 4.7, 0.0])
distance_list.append([address_list[13], 5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0])
distance_list.append([address_list[14], 4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0])
distance_list.append([address_list[15], 3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0])
distance_list.append([address_list[16], 7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0])
distance_list.append([address_list[17], 2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0])
distance_list.append([address_list[18], 3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0])
distance_list.append([address_list[19], 6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0])
distance_list.append([address_list[20], 1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0])
distance_list.append([address_list[21], 3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2,	10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0])
distance_list.append([address_list[22], 2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0])
distance_list.append([address_list[23], 6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5, 0.0])
distance_list.append([address_list[24], 2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0.0])
distance_list.append([address_list[25], 5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9, 6.8, 10.6, 7.0, 0.0])
distance_list.append([address_list[26], 3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0.0])

######################################################################
# Returns the distance between two addresses.
# O(1)
# 
######################################################################
def find_distance(start, end):
    finish = address_list.index(end)
    begin = address_list.index(start)
    
    if begin >= finish:
        return distance_list[begin][finish+1]
    elif finish >= begin:
        return distance_list[finish][begin+1]
    else:
        return 0.0

######################################################################
# Takes the current locations and finds the nearest from a given list.
# current = street address string
# p_list = list of package ids
#
# O(n)
# 
###################################################################### 
def find_next(current, p_list):
    next = ''
    closest = 1000.0

    for p in p_list:
        dist = find_distance(current, package_list.my_hash_lookup(p).street)
        if dist < closest:
            closest = dist
            next = package_list.my_hash_lookup(p)
    
    return (closest, next)

######################################################################
# Splits a Package List among 4 trucks.
# O(n^2)
# 
# (Revision: Added another load for special notes.)
######################################################################    
def split_packages():
    load1 = []
    load2 = []
    load3 = []
    load4 = []
    remaining_packages = []

    # Loads a list of package IDs to distribute between trucks 
    remaining_packages = package_list.get_IDs()

    for x in remaining_packages:
        if package_list.my_hash_lookup(x).notes == 'Can only be on truck 2*':
            load4.append(x)
            remaining_packages.remove(x)

    # Selects Priority packages without notes
    for p in remaining_packages:
        if (package_list.my_hash_lookup(p).deadline != 'EOD') and (package_list.my_hash_lookup(p).notes == '*'):
            load1.append(package_list.my_hash_lookup(p).id)
        else:
            load3.append(package_list.my_hash_lookup(p).id)

    # Selects shared delivery addresses without notes
    for i in load1:
        for x in load3:
            if (package_list.my_hash_lookup(i).street == package_list.my_hash_lookup(x).street) and (len(package_list.my_hash_lookup(x).notes) == 1):
                load1.append(x)
                load3.remove(x) 

    # Selects Priority packages and delayed arrivals 
    for i in load3:
        if (package_list.my_hash_lookup(i).deadline != 'EOD') or (package_list.my_hash_lookup(i).notes.split(' ')[0] == 'Delayed'):
            load2.append(i)
            load3.remove(i)
          
    # Selects matching address or matching zipcodes to fill out manifest. Restricts packages with note about truck usage.
    for i in load2:
        for x in load3:
            if (package_list.my_hash_lookup(i).street == package_list.my_hash_lookup(x).street) or (package_list.my_hash_lookup(i).zipcode == package_list.my_hash_lookup(x).zipcode):
                load2.append(x)
                load3.remove(x)

    return(load1, load2, load3, load4)

######################################################################
# Routing Function
# Takes a list of Package IDs and the number of minute after 8AM
# Prints relevant info and returns total minutes traveled, total distance traveled, and ending time.
# O(n^2) ('While' loop uses (find_next) function containinig a 'for' loop)
#
# (Revision: Added a second list of priority packages to loop through before the rest. )
######################################################################
def route(p_list, time_left_hub, first_load):
    total_dist = 0.0
    hub = address_list[0]
    now  = hub 
    total_minutes = 0.0
    miles_per_min = 18/60
    depart = '{}:{:02}'.format(int(time_left_hub/60) + 8, int(time_left_hub%60))
    current_time_in_min = '{}:{:02}'.format(int(time_left_hub/60) + 8, int(time_left_hub%60))
    priority_list = []
    packages = p_list[:]

    
    for p in packages:
        if package_list.my_hash_lookup(p).deadline != 'EOD':
            priority_list.append(package_list.my_hash_lookup(p).id)
    
    for p in priority_list:
        if p in packages:
            packages.remove(p)
    
    # Iterates through the list of packages, finds the next closest, updates delivery status, and removes package from vehicle manifest.
    # Iterates through priority list first.
    while p_list:      
        while priority_list:
            next = find_next(now, priority_list)
            total_dist = total_dist + next[0]
            now = next[1].street
            total_minutes = total_minutes + (next[0]/miles_per_min)
            current_time_in_min = time_left_hub + total_minutes
            #current_time = '{}:{:02}'.format(int(current_time_in_min/60) + 8, int(current_time_in_min%60))
            package_list.my_hash_lookup(next[1].id).status = "{}:{:02}".format(int(current_time_in_min/60)+8, int(current_time_in_min%60))
            priority_list.remove(next[1].id)
            p_list.remove(next[1].id)
        
        next = find_next(now, p_list)
        total_dist = total_dist + next[0]
        now = next[1].street
        total_minutes = total_minutes + (next[0]/miles_per_min)
        current_time_in_min = time_left_hub + total_minutes
        #current_time = '{}:{:02}'.format(int(current_time_in_min/60) + 8, int(current_time_in_min%60))
        package_list.my_hash_lookup(next[1].id).status = "{}:{:02}".format(int(current_time_in_min/60)+8, int(current_time_in_min%60))
        p_list.remove(next[1].id)
    # Adds travel distance to return to hub.
    if first_load:
        if len(p_list) == 0:
            distance = find_distance(now, hub)
            total_dist = total_dist + distance

    print('Departure Time: {}'.format(depart))
    print('Total route distance: {:.2f} miles'.format(total_dist))
    print('Total Time Traveled: {} hour/s and {} minutes'.format(int(total_minutes/60), int(total_minutes%60)))
    all_delivered_time = '{}:{:02}'.format(int(current_time_in_min/60)+8, int(current_time_in_min%60))
    print('Time when truck returns to Hub after all packages delivered:  {}:{:02}'.format(int(current_time_in_min/60)+8, int(current_time_in_min%60)))

    return (total_minutes, total_dist, all_delivered_time)

######################################################################
# Takes a Time in 00:00 format and returns all package status.
# O(n)
# (Revision: Updated formatting)
######################################################################
def all_packages_now(t):
    p_ids = package_list.get_IDs()
    packages_now = []
    d_time = datetime.datetime.strptime(t, '%H:%M')
    business_start = datetime.datetime.strptime('8:00', '%H:%M')
    statuses = []

    for p in p_ids:
            packages_now.append((p, datetime.datetime.strptime(package_list.my_hash_lookup(p).status, '%H:%M')))

    for i in packages_now:
        if i[1] < business_start:
            statuses.append((i[0], 'Package ID: {}........Status: At the hub'.format(i[0])))
        elif i[1] > d_time and i[1] > business_start:
            statuses.append((i[0], 'Package ID: {}........Status: En Route'.format(i[0])))
        else:
            statuses.append((i[0], 'Package ID: {}........Status: Delivered at {}'.format(i[0], i[1].strftime('%H:%M'))))

    for i in range(1,40):
        for x in statuses:
            if i == x[0]:
                print(x[1])

    return packages_now

######################################################################
#   Function to Deliver Packages.
# Terminal printing formatting and truck routing to simulate delivery.
# 
# (Revision: Added a second load for truck 2 to accomodate special notes.)
######################################################################
def execute_business_day(trucks):
    print('***************************')
    #print(trucks[0])                      # Print Truck 1 Package ID list.
    truck1_progress = route(trucks[0], 0.0, True)    
    print('***************************')
    #print(trucks[1])                      # Print Truck 2 Package ID list.
    trusk2_progress = route(trucks[1], 65.0, True) # leaves hub at 9:05am after package address is updated.
    print('***************************')
    #print(trucks[2])                      # Print Truck 3 (truck 1 second load) Package ID list.
    truck3_progress = route(trucks[2], 140.0, False) # truck 1 second load
    print('***************************')
    #print(trucks[3])                       # Print truck 2 (second load) Package ID list
    truck4_progress = route(trucks[3], 169.0, False) # truck 2 second load leaves hub at 10:49 once previous load is delivered.
    print('***************************')
    print('Total Distance Driven: {}'.format((truck1_progress[1]+trusk2_progress[1]+truck3_progress[1]+truck4_progress[1])))
    print('***************************')


truck_lists = split_packages()
execute_business_day(truck_lists)

print('***************************************************************')
print('Hello! The packages have been sorted.')
input = input('Please Enter a Time of Day to Check Package Status: (Ex. "12:00"): ')
all_packages_now(input)

