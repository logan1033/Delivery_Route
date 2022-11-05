# Basic Hash functions for a list of tuples.
from Package import Package

######################################################################
# Basic Hash function. 
# Takes a Package object, takes the ID, and returns a key (ID%10)
# The package ID seems to be a direct incremental count. %10 works fine for under 100 packages. 
# Can be modified for pargeer package lists. (Ex. %1000)
######################################################################
def my_hash(package):
    key = package.id % 10
    return key

######################################################################
# Hash Table
# Creates a List of Lists (default = 10)
# 
######################################################################
class My_Hash:
    def __init__(self, buckets = 10):
        self.table = []
        for i in range(buckets):
            self.table.append([])

######################################################################
# Basic Hash function. 
# Takes a Package object, takes the ID, and returns a key (ID%10)
# The package ID seems to be a direct incremental count. %10 works fine for under 100 packages. 
# Can be modified for pargeer package lists. (Ex. %1000)
######################################################################
    def my_hash(self, package):
        key = package.id % 10
        return key

######################################################################
# Hash Table Lookup
# Takes a package ID and a list to search and returns the pacakge object.
######################################################################
    def my_hash_lookup(self, package_id):
        key = package_id % len(self.table)
        for i in self.table[key]:
            if i.id == package_id:
                return i
    

######################################################################
# Hash Insert
# Take and object and a list. Creates a hash key from the object and adds it to the list.
######################################################################
    def my_hash_insert(self, item):
        key = my_hash(item)
        list = self.table[key]
        list.append(item)


######################################################################
# Hash Table Remove
# Take and Object and a list, removes the object from the list.
######################################################################
    def my_hash_remove(item, item_list):
        key = my_hash(item[1])
        item_list[key].remove(item)

######################################################################
# Hash Table getIDs
# Returns a list of all package IDs from the entire table.
######################################################################
    def get_IDs(self):
        ids = []
        for i in self.table:
            for x in i:
                ids.append(x.id)
        return ids