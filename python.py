import os
os.system('cls')

bidder_list = []

bool = True

while bool:
    name = input("Your name: ")
    bid = input("Your bid amount: $")
    bidder_list.append({'name': name, 'bid': bid})
    loop = input("Are there any other bidder? yes or no: ")
    os.system('cls')
    if loop == 'no':
        bool = False
     
max_bid = bidder_list[0]['bid']
max_bid_name = bidder_list[0]['name']  
for key in bidder_list:
    if key['bid'] > max_bid:
        max_bid = key['bid']
        max_bid_name = key['name']

print(f"The winner is {max_bid_name} with a bid of ${max_bid}")

 
    