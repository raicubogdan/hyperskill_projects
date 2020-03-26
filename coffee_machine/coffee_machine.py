# Simulation a real world coffee machine 
# (resources, buy function, refill function, interface)

# Defining the state of the coffee_machine and 
# the cost of the products. Each of them has a 
# lenght of 5, so we can easily iterate of them
resources = ['water', 'milk', 'beans', 'cups', 'money']
state = [400, 540, 120, 9, 550]
espresso = [250, 0, 16, 1, -4]
latte = [350, 75, 20, 1, -7]
cappuccino = [200, 100, 12, 1, -6]

def check(tip):
    """Checks if the coffee_machine has enough
    resources to make the specified product"""
    for i, _ in enumerate(tip):
        if state[i] < tip[i]:
            return i
    return i

def buy(tip):
    """ Subtracts resources from the coffee_machine
    and adds money """
    if tip == '1':
        tip = espresso
    elif tip == '2':
        tip = latte
    else:
        tip = cappuccino

    index = check(tip)

    if index == 4:
        print("I have enough resources, making you a coffee!")
        for i, _ in enumerate(tip):
            state[i] -=  tip[i]
    else:
        print(f'Sorry, not enough {resources[index]}!')
    
def fill():
    """Refills coffee_machine resources"""

    state[0] += int(input('Write how many ml of water do you want to add:'))
    state[1] += int(input('Write how many ml of milk do you want to add:'))
    state[2] += int(input('Write how many grams of coffee beans do you want to add:'))
    state[3] += int(input('Write how many disposable cups of coffee do you want to add:'))

def display():
    "coffee_machine interface"
    print(f'''
The coffee machine has:
{state[0]} of water
{state[1]} of milk
{state[2]} of coffee beans
{state[3]} of disposable cups
{state[4]} of money 
''')

while True:
    action = input('Write action (buy, fill, take, remaining, exit):')

    if action == 'take': # Gets the money from the coffee_machine
        print(f'I gave you ${state[4]}')
        state[4] = 0
        
    elif action == 'fill':
        fill()
        
    elif action == 'buy':
        action = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if action != 'back':
            buy(action)
        else:
            pass

    elif action == 'remaining':
        display()
        
    else:
        exit()
