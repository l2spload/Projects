#Flow Control

weight = 41.5

#Ground Shipping
if weight <= 2:
  ground_cost = weight * 1.50 + 20
elif 2 < weight <= 6:
  ground_cost = weight * 3.00 + 20
elif 6 < weight <= 10:
  ground_cost = weight * 4.00 + 20
elif weight > 10:
  ground_cost = weight * 4.75 + 20
else:
  print('Invalid Weight')

print("Ground Shipping costs: {}".format(round(ground_cost, 2)))

#Ground Shipping Premium
ground_premium_cost = 125.00

print("Ground Shipping Premium costs: {}".format(ground_premium_cost))

#Drone Shipping
if weight < 2:
  drone_shipping_cost = weight * 4.50
elif 2 < weight <= 6:
  drone_shipping_cost = weight * 9.00
elif 6 < weight <= 10:
  drone_shipping_cost = weight * 12.00
elif weight > 10:
  drone_shipping_cost = weight * 14.25
else:
  print('Invalid Weight')

print("Drone Shipping costs: {}".format(round(drone_shipping_cost, 2)))

#-------------------------------------------------------------------------#

#Lists

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[-1][1] = 98

gradebook[2].remove(85)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)

#-----------------------------------------------------------------#

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print('We cell {} different kinds of pizza!'.format(num_pizzas))

pizza_and_prices = [list(n) for n in zip(prices, toppings)]

#pizza_and_prices = []
#i  = 0
#while i < len(toppings):
#  pizza_and_prices[i].insert([prices[i], toppings[i]])
#  i += 1

pizza_and_prices.sort()

print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(4, [2.5, 'peppers'])

print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]

#------------------------------------------------------#

#Loops

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for p in prices:
  total_price += p

average_price = total_price / len(prices)

print("Average Haircut Price: {}".format(average_price))

new_prices = [p - 5 for p in prices]

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i]
  total_revenue += last_week[i]

print("Total Revenue: {}".format(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)

#----------------------------------------------------------------------------------------#

#Functions

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  c_temp = f_temp - 32 * 5/9

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies {} Newtons of force.".format(train_force))

c = 3 * 10 ** 8 
def get_energy(mass, c):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies {} Joules.".format(bomb_energy))

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))

#-------------------------------------------------------------------------------------------------#

#Strings

daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""


daily_sales_replaced = daily_sales.replace(';,;', '|')

daily_transactions = daily_sales_replaced.split(',')

#print(daily_transactions)

daily_transactions_split = []

for n in daily_transactions:
  daily_transactions_split.append(n.split('|'))

#print(daily_transactions_split)

transactions_clean = []

for lists in daily_transactions_split:
  transaction_clean = []
  for i in lists:
    transaction_clean.append(i.replace("\n", "").strip(" "))
    transactions_clean.append(transaction_clean)

#print(transactions_clean)

customers = []
sales = []
thread_sold = []

for n in transactions_clean:
  
  customers.append(n[0])
  sales.append(n[1])
  thread_sold.append(n[2]) 

#print(customers)
#print(sales)
#print(thread_sold)

total_sales = 0

for s in sales:
  total_sales += float(s.strip("$"))

#print(total_sales)

#print(thread_sold)

thread_sold_split = []

for thread in thread_sold:
  for color in thread.split("&"):
    thread_sold_split.append(color)

def color_count(color):
  color_total = 0
  for n in thread_sold_split:
    if color == n:
      color_total += 1
  return color_total

color_count('white')

colors = ['red','yellow','green','white','black','blue','purple']

for color in colors:
  num_color = color_count(color)
  print("Thread Shed sold {} threads of {} thread today.".format(num_color, color))


#------------------------------------------------------------------------------------#


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  word_counter = 0
  for n in letters:
    if n in word:
      word_counter += 1
  return word_counter

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


#--------------------------------------------#

def count_char_x(word, x):
  letter_occ = 0
  for n in word:
    if x == n:
      letter_occ += 1
  return letter_occ


#---------------------------------------------#

def count_multi_char_x(word, x):
  splits = word.split(x)
  print(splits)
  return(len(splits)-1)

#---------------------------------------------#

def substring_between_letters(word, start, end):
  letter_start = word.find(start)
  letter_end = word.find(end)
  if letter_start == -1 or letter_end == -1:
    return word
  else:
    return word[letter_start + 1:letter_end]

#--------------------------------------------#

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

#--------------------------------------------#

def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] + ' ' + word1[0] + word2[1:]

#Dictionaries

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for w in word:
    if w in letters:
      point_total += letter_to_points[w]
    else:
      print("{} is not in list.".format(w))
  return point_total

brownie_points = score_word("BROWNIE")
#print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

#--------------------------------------------#

def sum_values(my_dictionary):
  dict_sum = 0
  for value in my_dictionary.values():
    dict_sum += value
  return dict_sum

#----------------------------------------#

def sum_even_keys(my_dictionary):
  total_val = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total_val += my_dictionary[key]
  return total_val

#----------------------------------------#

def add_ten(my_dictionary):
  for n in my_dictionary.keys():
    my_dictionary[n] += 10
  return my_dictionary

#----------------------------------------#

def values_that_are_keys(my_dictionary):
  new_lst = []
  for v in my_dictionary.values():
    if v in my_dictionary:
      new_lst.append(v)
  return new_lst

#----------------------------------------#

def max_key(my_dictionary):
  large_value = 0
  large_key = 0
  for k, v in my_dictionary.items():
    if v > large_value:
      large_value = v
      large_key = k
  return large_ke

#-----------------------------------------#

def word_length_dictionary(words):
  word_len = {}
  for word in words:
    word_len[word] = len(word)
  return word_len

#-----------------------------------------#

def count_first_letter(names):
  new_dict = {}
  for k in names:
    if k[0] not in new_dict:
      new_dict[k[0]] = 0
    new_dict[k[0]] += len(names[k])
  return new_dict

#-----------------------------------------#



#Files

import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for user_row in compromised_users:
    compromised_user_file.write(user_row)

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = '''
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''

  new_passwords_obj.write(slash_null_sig)

#--------------------------------------------------------------#

#Classes/OOP

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {} - {}".format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for n in purchased_items:
      if n in self.items:
        bill += self.items[n]
    return bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)
early_bird_menu.calculate_bill(['salumeria plate', 'vegan mushroom ravioli'])

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, 1100, 2100)

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

flagship_store.available_menus(1200)
flagship_store.available_menus(1700)

first_business = Business("Basta Fazoolin' with my Heart", ['flagship_store', 'new_installment'])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a Arepa', arepas_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

arepas_business = Business('Take a Arepa', [arepas_place])

#--------------------------------------------------------------#

class DriveBot:

  all_disabled = False
  latitude = -999999
  longitude = -999999
  robot_count = 0

  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range
    DriveBot.robot_count += 1
    self.id = DriveBot.robot_count
    
  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction

  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

#--------------------------------------------------#

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

    def avoid_obstacles(self):
       if(self.obstacle_found):
           if(self.speed <= 60):
               super().avoid_obstacles()
           else:
               self.direction = (self.direction + 90) % 360
               self.obstacle_found = False
           self.speed /= 2
           self.step_length /= 2

    def __add__(self, value):
       super().__add__(value)
       self.step_length += value / 2

    def __sub__(self, value):
       super().__sub__(value)
       self.step_length -= value / 2

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)

#---------------------------------------#

