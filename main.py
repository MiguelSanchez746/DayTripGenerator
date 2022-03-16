import random

random_destinations = ['Hawaii', 'Greece', 'Rome', 'England'] 
random_restaurants = ['La Mer Senia', '53 by the sea', 'nYlos', 'Canoehouse'] 
random_transportations = ['Plane','Bus','Boat'] 
random_entertainment = ['Movies','Tour','Night Club','Spa'] 


def get_random_destintation(passed_in_random_destination):
 destination = random.choice(passed_in_random_destination)
passed_in_random_destination = random.choice(random_destinations)
your_destination_choice= input(f'would you like to visit {passed_in_random_destination}? ') 
if your_destination_choice == 'yes':
    print('perfect') 
if your_destination_choice == 'no': 
    print(f'no worries, how about {passed_in_random_destination}?') 


def eat_at_random_restaruant(passed_in_random_restarant):
    restaurant = random.choice(passed_in_random_restarant) 
passed_in_random_restaurant = random.choice(random_restaurants) 
your_restaurant_choice= input(f'would you like to eat at {passed_in_random_restaurant} ') 
if your_restaurant_choice == 'yes':
    print('prefect')
if your_restaurant_choice == "no":
    print(f'no worries, how about {passed_in_random_restaurant}') 


def how_would_you_like_to_transport(passed_in_random_transportation):
    transportation = random.choice(passed_in_random_transportation)
passed_in_random_transportation = random.choice(random_transportations) 
your_transportation_choice = input(f'would you like to transpory by {passed_in_random_transportation}? ') 
if your_transportation_choice == 'yes':
 print('perfect') 
if your_transportation_choice == 'no': 
 print (f'no worries, how about {passed_in_random_transportation}') 

 def what_would_you_like_do(passed_in_random_entertainment):
     entertainment = random.choice(passed_in_random_entertainment)
passed_in_random_entertainment = random.choice(random_entertainment)
your_entertainment_choice = input(f'what would you like to {passed_in_random_entertainment}? ') 
if your_entertainment_choice == 'yes':
 print('perfect') 
if your_entertainment_choice == 'no':
    print(f'no worries, how about {passed_in_random_entertainment}') 
if passed_in_random_entertainment and passed_in_random_destination and passed_in_random_restaurant and passed_in_random_transportation=='yes':
 print('awsome your all set') 