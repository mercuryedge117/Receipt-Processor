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
    
    # Examine retailer points increment
    point += processRetailer(retailer)
    
    # Convert and examine total price
    point += processTotal(float(total))
    
    # Convert and examine purchase day and time
    purchase_date = datetime.strptime(purchaseDate, '%Y-%m-%d')
    purchase_time = datetime.strptime(purchaseTime, '%H:%M')
    point += processDateTime(purchase_date, purchase_time)

    # Handle the items point calculation
    point += processItem(items)

    return point

def processRetailer(name_):
    localPoint = 0

    # iterate through retailer to get point for each alphanumeric character 
    for char in name_:
        if char.isalpha():
            localPoint += 1
    
    return localPoint

def processTotal(total_num):
    localPoint = 0

    # check total is round or not 
    if total_num == int(total_num):
        localPoint += 50

    # check total is multiple of 0.25
    if total_num % 0.25 == 0:
        localPoint += 25

    return localPoint

def processDateTime(date_, time_):
    localPoint = 0

    # check if purchaseDate is odd
    if date_.day % 2 != 0:
        localPoint += 6

    # check if purchaseTime is between 14:00 to 16:00
    start_time = time(14, 0)
    end_time = time(16, 0)
    if (start_time <= time_.time() < end_time):
        localPoint += 10
    
    return localPoint

def processItem(items):
    localPoint = 0

    # add 5 point for every 2 items
    localPoint += int(len(items) / 2) * 5
    # Calculate point earn for each items
    for item_dict in items:
        description = item_dict.get("shortDescription")
        price = item_dict.get("price")

        if description is None or price is None: 
            raise Exception("Items incomplete")
        
        description_trim = description.strip()
        if len(description_trim) % 3 == 0:
            localPoint += math.ceil(float(price) * 0.2)
    
    return localPoint