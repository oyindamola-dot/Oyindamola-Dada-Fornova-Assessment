#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import json

# Loading the JSON file
file_path = "C:/Users/hp/Downloads/Python-task.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert the 'assignment_results' list into a DataFrame
df_assignment = pd.json_normalize(data['assignment_results'])

# Convert the 'aux_data' dictionary into a DataFrame
df_aux = pd.json_normalize(data['aux_data'])

# Display the resulting DataFrames
print("Assignment Results DataFrame:")
df_assignment

print("\nAuxiliary Data DataFrame:")
df_aux


# In[20]:


import pandas as pd
# Step 1: unpivot the data using pd.melt()
df_longer = pd.melt(df, 
                       var_name='Category', 
                       value_name='Value')

# Step 3: Show the unpivoted DataFrame
print("Unpivoted DataFrame:")
display(df_longer)


# In[64]:


#question 1: Find and return the cheapest(lowest) shown price (Please avoid using the minimum function)

import pandas as pd

data = {'shown_price': [113.05, 90, 115.05, 112.05]}
df = pd.DataFrame(data)

# Initialize a variable to a large number or the first element of the column
lowest_price = float('inf')

# Loop through each value in the 'shown_price' column
for price in df['shown_price']:
    if price < lowest_price:
        lowest_price = price

print("Cheapest shown price:", lowest_price)

df_cheapest_shown_price = pd.DataFrame(cheapest_room_data)

# Save to CSV
output_csv_path = 'C:/Users/hp/Downloads/Cheapest_shown_price.csv'
df_cheapest_shown_price.to_csv(output_csv_path, index=False)

print(f"The details of the cheapest shown price have been saved to {output_csv_path}")


# In[69]:


# question number two: Find and return the room type, number of guest with the cheapest price

import pandas as pd

# Sample data for demonstration
data = {
    'room_type': ["King Studio Suite - Non Smoking", "Queen Suite with Two Queen Beds - Non-Smoking", 
                  "King Room - Mobility/Hearing Accessible - Non-Smoking", "King Studio Suite - Hearing Accessible/Non-Smoking"],
    'number_of_guests': [4, 2, 2, 3],
    'shown_price': [90, 112.05, 115.05, 113.05]
}
df = pd.DataFrame(data)

# Initialize variables to store the lowest price and corresponding details
lowest_price = float('inf')
cheapest_room_type = None
cheapest_number_of_guests = None

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    if row['shown_price'] < lowest_price:
        lowest_price = row['shown_price']
        cheapest_room_type = row['room_type']
        cheapest_number_of_guests = row['number_of_guests']

# Display the result
print("Cheapest Price Details:")
print("Room Type:", cheapest_room_type)
print("Number of Guests:", cheapest_number_of_guests)
print("Price:", lowest_price)

# Save to CSV
output_csv_path = 'C:/Users/hp/Downloads/room_type_and_the_no_of_guest_with_the_cheapest_price.csv'
df_cheapest_room.to_csv(output_csv_path, index=False)

print(f"The details of the room type, number of guest with the cheapest price {output_csv_path}")


# In[68]:


#Question number 3: Print the total price (Net price + taxes) for all rooms along with the room type

import pandas as pd
import json

# my data
data = {
    'room_type': ["King Studio Suite - Non Smoking", "Queen Suite with Two Queen Beds - Non-Smoking", 
                  "King Room - Mobility/Hearing Accessible - Non-Smoking", "King Studio Suite - Hearing Accessible/Non-Smoking"],
    'net_price': [90, 112.05, 115.05, 113.05],
    'taxes': ['{ "TAX": "14.70", "City tax": "4.01"}', '{ "TAX": "14.70", "City tax": "4.01"}', 
              '{ "TAX": "14.70", "City tax": "4.01"}', '{ "TAX": "14.70", "City tax": "4.01"}']
}
df = pd.DataFrame(data)

# Function to calculate total price for each room
def calculate_total_price(row):
    # Parse the taxes JSON string
    taxes = json.loads(row['taxes'])
    
    # Convert tax values to floats and calculate the sum
    total_tax = sum(float(value) for value in taxes.values())
    
    # Calculate the total price by adding net price and total taxes
    total_price = row['net_price'] + total_tax
    return total_price

# Open a file in write mode to save the output
output_file_path = 'C:/Users/hp/Downloads/total_price_for_all_rooms_with_room_type.csv'
with open(output_file_path, 'w') as file:
    # Write each room type and its total price to the file
    for room_type, total_price in zip(room_types, total_prices):
        file.write(f"Room Type: {room_type}, Total Price: {total_price:.2f}\n")

print(f"Output has been written to {output_file_path}")


# In[ ]:




