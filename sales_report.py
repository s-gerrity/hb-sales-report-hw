"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

# Turn our sales file into a list
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    # Assign index 0 as salespeople names
    # Assign index of melons sold
    salesperson = entries[0]
    melons = int(entries[2])

    # Match the salesperson in the list to their melons sold and 
    # 
    if salesperson in salespeople: # take names
        position = salespeople.index(salesperson) # find the name in the list and the location is indexed at "position"
        

        melons_sold[position] += melons # where the salesperson is in the list we take the 
                                        # associated melons sold and add to the melons sold list to align with their name

    else:
        salespeople.append(salesperson) # if their name has not yet been added to the salesperson list, do it now
        melons_sold.append(melons)      # and add the melons sold to the list, this way they can all be matched together in the loop

# prints the statement matching names with sales
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
