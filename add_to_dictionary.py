#the purpose of this code is to quickly put together a large python dictionary

list_of_data = [] #an empty list of data to be in the qrcodes
list_of_names = [] #an empty list of the names of the qrcodes that will be associated with data

n = 1 #setting up the loop: this will be sample 1
while n <= 10: #here is where you can change the number of samples in the list
    list_of_data.append('Sample'+str(n)) #adding the sample number to the list
    list_of_names.append('SAMPLE_'+str(n)) #adding the sample name to the list
    n = n + 1 #adding one to n to go through the loop

dict_of_associated_data = dict(zip(list_of_data, list_of_names)) #connecting the lists into a dictionary
print(dict_of_associated_data) #printing the dictionary to check that it's correct
