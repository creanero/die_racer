import random
import numpy as np
import matplotlib.pyplot as plt
import time


def roll_die(sides=6, print_results=False):
    # randomly generates an integer between 1 and sides
    # returns that integer
    # prints to std.out if print_results is true
    roll = random.randint(1, sides)

    if print_results:
        print("roll d{}: {}".format(sides, roll))

    return roll


def roll_many(dice=1, sides=6, print_results=False):
    rolls = []

    for die in range(dice):
        roll = roll_die(sides=sides, print_results=print_results)
        rolls.append(roll)

    if print_results:
        print("{} rolls of d{}: {}".format(dice, sides, rolls))

    return rolls


def create_results(rolls=20, dice=1, sides=6, print_results=False):
    results = []
    for roll in range(rolls):
        result = sum(roll_many(dice=dice, sides=sides, print_results=print_results))
        results.append(result)
    if print_results:
        print("{} results of {}d{}: {}".format(rolls, dice, sides, results))
    return results


def running_totals(splits=None, print_results=False):
    if splits is None:
        splits = []
    total = 0
    totals = []
    for result in splits:
        total = total + result
        totals.append(total)

    if print_results:
        print("Running totals = " + str(totals))

    return totals


def race(rolls=20, dice_1=1, sides_1=6, dice_2=1, sides_2=8, print_results=False):
    results_1 = np.array(create_results(rolls=rolls,
                                        dice=dice_1,
                                        sides=sides_1,
                                        print_results=print_results))

    results_2 = np.array(create_results(rolls=rolls,
                                        dice=dice_2,
                                        sides=sides_2,
                                        print_results=print_results))

    splits = results_2 - results_1

    if print_results:
        print("{} splits of {}d{} against {}d{}: {}".format(rolls, dice_1, sides_1, dice_2, sides_2, splits))

    return splits


def total_race(rolls=20, dice_1=1, sides_1=6, dice_2=1, sides_2=8, print_results=False):
    splits = race(rolls=rolls,
                   dice_1=dice_1, sides_1=sides_1,
                   dice_2=dice_2, sides_2=sides_2,
                   print_results=print_results)
    totals = running_totals(splits=splits, print_results=print_results)

    if print_results:
        print("{} running totals of {}d{} against {}d{}: {}".format(rolls, dice_1, sides_1, dice_2, sides_2,totals))

    return totals


def many_races(races=10, rolls=20, dice_1=1, sides_1=6, dice_2=1, sides_2=8, print_results=False):
    tracks = []

    for race in range(races):
        if print_results:
            print("Race " + str(race + 1) + ":")

        tracks.append(total_race(rolls=rolls,
                                 dice_1=dice_1, sides_1=sides_1,
                                 dice_2=dice_2, sides_2=sides_2,
                                 print_results=print_results)
                      )

    return tracks


def plot_tracks(tracks, title=''):
    for track in tracks:
        plt.plot(track)

    plt.title(title)
    plt.ylabel('Total result')
    plt.xlabel('Number of rolls')
    plt.axhline(y=0, color='k')
    plt.show()


def main():
    races = 10
    rolls = 100
    dice_1 = 1
    sides_1 = 6
    dice_2 = 1
    sides_2 = 8
    print_results = False

    title = "Plot of {} races of {}d{} against {}d{} rolled {} times".format(races,
                                                                             dice_1,
                                                                             sides_1,
                                                                             dice_2,
                                                                             sides_2,
                                                                             rolls)
    start_time = time.time()

    tracks = many_races(races=races,
                        rolls=rolls,
                        dice_1=dice_1,
                        sides_1=sides_1,
                        sides_2=sides_2,
                        dice_2=dice_2,
                        print_results=print_results)

    end_time = time.time()

    run_time = end_time-start_time

    print("Run time: {:.4g}s".format(run_time))

    plot_tracks(tracks, title)


if __name__ == '__main__':
    main()
