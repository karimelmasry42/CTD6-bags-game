import random
import cv2
import os
bags: list = [10, 10, 10]
turn: bool = 0  # 0 for human, 1 for bot
USERNAME: str = input('Enter username: ')
USER_WON_PATH: str = os.getcwd() + '/Images/user_won.png'
BOT_WON_PATH: str = os.getcwd() + '/Images//bot_won.png'
USER_WON_IMG: cv2.Mat = cv2.putText(
    cv2.imread(USER_WON_PATH),
    f'{USERNAME} WON!',
    (100, 500),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (255, 0, 0),
    5,
    cv2.LINE_AA,
    False
)
BOT_WON_IMG: cv2.Mat = cv2.putText(
    cv2.imread(BOT_WON_PATH),
    'BOT WON!',
    (100, 500),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (255, 0, 0),
    5,
    cv2.LINE_AA,
    False
)


def print_bags() -> None:
    print(f'''
    Bag 1 has {bags[0]} objects
    Bag 2 has {bags[1]} objects
    Bag 3 has {bags[2]} objects
''')


def choose_bag() -> int:
    '''returns bag number (index + 1)'''
    try:
        i: int = int(input('Choose a non-empty bag: '))
        if (1 <= i <= 3) and bags[i-1] != 0:
            return i
    except:
        pass
    print('Invalid input')
    return 0


def input_amount(bag_index: int) -> int:
    try:
        r: int = int(input(
            'Enter amount to remove (1 to 5 and less than in bag): '))
        if (1 <= r <= 5) and r <= bags[bag_index]:
            return r
    except:
        pass
    print('Invalid input')
    return 0


def human() -> None:
    while True:
        bag: int = choose_bag()
        if bag == 0:
            continue
        amount: int = input_amount(bag - 1)
        if amount == 0:
            continue
        break
    bags[bag-1] -= amount
    print(f'{USERNAME} removed {amount} from bag {bag}, so')
    print_bags()
    global turn
    turn = 1 - turn


def bot():
    non_empty = [(i, val) for (i, val) in enumerate(bags) if val != 0]
    # choose a bag
    bag_tuple: tuple = random.choice(non_empty)
    bag_index: int = bag_tuple[0]
    bag_amount: int = bag_tuple[1]
    # remove amount
    max_amount: int = 5 if bag_amount >= 5 else bag_amount
    amount: int = random.randint(1, max_amount)
    bags[bag_index] -= amount
    print(f'BOT removed {amount} from bag {bag_index + 1}, so')
    print_bags()
    global turn
    turn = 1 - turn


print_bags()
while True:
    human()
    if all(bag == 0 for bag in bags):
        break
    bot()
    if all(bag == 0 for bag in bags):
        break
if turn:
    cv2.imshow(f'{USERNAME} won!', USER_WON_IMG)
else:
    cv2.imshow('BOT won!', BOT_WON_IMG)
cv2.waitKey(0)
