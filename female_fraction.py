
# http://www.thebigquestions.com/2010/12/27/win-landsburgs-money/

import random
import sys

# The number of simulated runs.
NUM_RUNS = 3000

def go(num_families):
    # sys.stderr.write("%d\n" % num_families)

    # Average of all the runs.
    total_fraction_female = 0

    # Do a bunch of runs to get a good average.
    for run in range(NUM_RUNS):
        # This is the total number of boys and girls in this country in this run.
        num_boys = 0
        num_girls = 0

        # Simulate each family having children until they have a boy.
        for family in range(num_families):
            # They keep trying.
            while True:
                # 50% chance of having a boy.
                if random.randint(0,1) == 0:
                    # Got a boy. Quit.
                    num_boys += 1
                    break
                else:
                    # Got girl. Keep trying.
                    num_girls += 1

        # The fraction is the number of girls divided the number of children.
        fraction_female = float(num_girls) / (num_girls + num_boys)

        # Add this to our average.
        total_fraction_female += fraction_female

    # Divide by the number of runs we had.
    total_fraction_female /= NUM_RUNS

    print("%d %g" % (num_families, total_fraction_female*100))

def main():
    print("Families [domain]\tFraction female")
    for num_families in range(1, 11):
        go(num_families)

if __name__ == "__main__":
    main()

