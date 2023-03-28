import matplotlib.pyplot as plt
import csv
import numpy as np


# grab random number from each column and report new list back
def random_numbers(*args, luckyballs):
    random_nums = []
    lucky_pick = np.random.choice(luckyballs)
    for arr in args:
        rand_pick = np.random.choice(arr)
        while rand_pick in random_nums:
            rand_pick = np.random.choice(arr)
        random_nums.append(rand_pick)
    print(f"Random Numbers {sorted(random_nums[0:5])}, lucky num: {lucky_pick}")

# calc the average value for each ball
def average_numbers(*args):
    average_nums = []
    for arr in args:
        average_nums.append(np.mean(arr, dtype=np.int_))
    print(f"Average Numbers {average_nums[0:5]}, lucky num: {average_nums[5]}")

# print the standard deviation for each column
def standard_devation(*args):
    std_nums = []
    for arr in args:
        std_nums.append(np.std(arr, dtype=np.int_))
    print(f"Standard Deviation {std_nums[0:5]}, lucky num: {std_nums[5]}")

def plot_hist(ball1, ball2, ball3, ball4, ball5, bins):
    fig = plt.figure(figsize=(10, 7))
    plt.hist(ball1, bins=bins, label="ball 1", edgecolor='black', linewidth=1)
    plt.hist(ball2, bins=bins, label="ball 2", edgecolor='black', linewidth=1)
    plt.hist(ball3, bins=bins, label="ball 3", edgecolor='black', linewidth=1)
    plt.hist(ball4, bins=bins, label="ball 4", edgecolor='black', linewidth=1)
    plt.hist(ball5, bins=bins, label="ball 5", edgecolor='black', linewidth=1)
    plt.legend(loc='upper right')
    plt.savefig('lucky4life.png')
    plt.show()

if __name__ == "__main__":
    FILTER_ALL = False
    BUCKET_SIZE = 65
    # list to store winning numbers
    winning_sets = []
    # list of ALL possible winning numbers
    balls_bins_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                   21,22,23,24,25,26,27,28,29,30,
                   31,32,33,34,35,36,37,38,39,40,
                   41,42,43,44,45,46,47,48]
    # open the csv file and create winning number list
    with open("csv/lucky_for_life.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row, values in enumerate(reader):
            winning_set = []
            # skip the first row of metadata values
            if row > 0:
                # split the winning nums apart into list
                winning_nums = values[1].split(",")
                # loop through winning nums and append to set
                for val in winning_nums:
                    winning_set.append(int(val))
                # append the lucky ball num and then append set to sets
                winning_set.append(int(values[2]))
                winning_sets.append(winning_set)

    # create numpy array from 2D list
    winning_balls = np.array(winning_sets)

    # grab all winning ball values
    if FILTER_ALL:
        winning_balls_1 = winning_balls[:, 0]
        winning_balls_2 = winning_balls[:, 1]
        winning_balls_3 = winning_balls[:, 2]
        winning_balls_4 = winning_balls[:, 3]
        winning_balls_5 = winning_balls[:, 4]
        lucky_balls = winning_balls[:, 5]
    # grab specified range of ball values
    else:
        winning_balls_1 = winning_balls[:BUCKET_SIZE, 0]
        winning_balls_2 = winning_balls[:BUCKET_SIZE, 1]
        winning_balls_3 = winning_balls[:BUCKET_SIZE, 2]
        winning_balls_4 = winning_balls[:BUCKET_SIZE, 3]
        winning_balls_5 = winning_balls[:BUCKET_SIZE, 4]
        lucky_balls = winning_balls[:BUCKET_SIZE, 5]

    random_numbers(winning_balls_1, winning_balls_2, winning_balls_3,
                   winning_balls_4, winning_balls_5, luckyballs=lucky_balls)
    average_numbers(winning_balls_1, winning_balls_2, winning_balls_3,
                   winning_balls_4, winning_balls_5, lucky_balls)
    standard_devation(winning_balls_1, winning_balls_2, winning_balls_3,
                   winning_balls_4, winning_balls_5, lucky_balls)
    '''
    plot_hist(winning_balls_1, winning_balls_2, winning_balls_3,
                   winning_balls_4, winning_balls_5, bins=balls_bins_values)
    '''