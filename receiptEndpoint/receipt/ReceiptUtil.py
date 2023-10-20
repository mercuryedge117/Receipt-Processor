import math
from datetime import datetime, time

def process(data_dict):

    retailer = data_dict.get("retailer")
    purchaseDate = data_dict.get("purchaseDate")
    purchaseTime = data_dict.get("purchaseTime")
    items = data_dict.get("items")
    total = data_dict.get("total")
    point = 0

    if (retailer is None or
        purchaseDate is None or
        purchaseTime is None or
        items is None or
        len(items) < 1 or
        total is None): 
        raise Exception("Receipt incomplete")

    # iterate through retailer to get point for each alphanumeric character 
    for char in retailer:
        if char.isalpha():
            point += 1
    
    # Convert and examine total price
    total_num = float(total)
    # check total is round or not 
    if total_num == int(total_num):
        point += 50
    # check total is multiple of 0.25
    if total_num % 0.25 == 0:
        point += 25
    
    # Convert and examine purchase day and time
    purchase_time = datetime.strptime(purchaseTime, '%H:%M')
    purchase_date = datetime.strptime(purchaseDate, '%Y-%m-%d')
    # check if purchaseDate is odd
    if purchase_date.day % 2 != 0:
        point += 6
    # check if purchaseTime is between 14:00 to 16:00
    start_time = time(14, 0)
    end_time = time(16, 0)
    if (start_time <= purchase_time.time() < end_time):
        point += 10

    # Handle the items point calculation
    # add 5 point for every 2 items
    point += int(len(items) / 2) * 5
    # Calculate point earn for each items
    for item_dict in items:
        description = item_dict.get("shortDescription")
        price = item_dict.get("price")
        if description is None or price is None: 
            raise Exception("Items incomplete")
        description_trim = description.strip()
        if len(description_trim) % 3 == 0:
            point += math.ceil(float(price) * 0.2)
    return point
        
        