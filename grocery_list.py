grocery_item = {} # Creating a dictionary
grocery_history = [] # Creating a list
stop = 'go'

while stop != 'q': # While loop to collect input
  item_name = input('Item name:\n')
  quantity = input('Quantity purchased:\n')
  cost = input('Price per item:\n')
  
  grocery_item = {'name':item_name, 'number':int(quantity), 'price':float(cost)} # Adding items to dictionary
  grocery_history.append(grocery_item) # Adding dictionary to list
  
  stop = input('Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')

grand_total = 0
  
for item in range(0,len(grocery_history),1): # Index based for loop for calculations
  item_total = float(grocery_history[item]['price']) * float(grocery_history[item]['number']) # Accessing items in dictionary in list
  grand_total += item_total
  
  print(str(grocery_history[item]['number']) + ' ' + str(grocery_history[item]['name']) + ' @ $' + 
  str(grocery_history[item]['price']) + ' ea $' + '{0:.2f}'.format(item_total)) # Accessing items in dictionary in list

  item_total = 0

print('Grand total: $' + '{0:.2f}'.format(grand_total))