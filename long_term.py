
# http://www.thebigquestions.com/2010/12/27/win-landsburgs-money/

from __future__ import division
import random

# The number of years to run the simulation.
NUM_YEARS = 3000

# Number of people to start out with.
INITIAL_POPULATION = 100

# Age where people can start having babies.
MIN_BABY_AGE = 20

# Age when people die.
DEATH_AGE = 40

# Enum for "sex" field.
MALE = "M"
FEMALE = "F"

# Represents a person in the simulation.
class Person(object):
    def __init__(self, sex, age=0):
        self.sex = sex
        self.age = age
        self.partner = None
        self.had_boy = False
        self.num_babies = 0

    def __repr__(self):
        return "(%s,%d)" % (self.sex, self.age)

def main():
    # All persons in the country.
    persons = []

    # Seed the population.
    for i in range(INITIAL_POPULATION//2):
        persons.append(Person(MALE, random.randint(0, MIN_BABY_AGE)))
        persons.append(Person(FEMALE, random.randint(0, MIN_BABY_AGE)))

    # Header for the Plotter program.
    print "Year [domain]\tPopulation\tRatio [right]"

    # Run the simulation.
    for year in range(NUM_YEARS):
        if len(persons) == 0:
            # Everyone died.
            break

        # Print statistics.
        num_males = sum(1 for p in persons if p.sex == MALE)
        num_females = sum(1 for p in persons if p.sex == FEMALE)
        ratio = num_females/len(persons)

        if False:
            print "%d total, %d male, %d female" % (
                    len(persons), num_males, num_females)

        # Data for the Plotter program.
        print year, len(persons), ratio

        # Find all single people.
        single_males = set(p for p in persons if p.sex == MALE and
                p.age >= MIN_BABY_AGE and p.partner is None)
        single_females = set(p for p in persons if p.sex == FEMALE and
                p.age >= MIN_BABY_AGE and p.partner is None)

        # Make new couples.
        while len(single_males) > 0 and len(single_females) > 0:
            m = single_males.pop()
            f = single_females.pop()
            m.partner = f
            f.partner = m

        # Make babies.
        coupled_males = set(p for p in persons if p.sex == MALE and
                p.partner is not None and not p.had_boy)
        for m in coupled_males:
            f = m.partner

            m.num_babies += 1
            f.num_babies += 1

            stop = False

            # 50% chance of having a boy.
            if random.randint(0,1) == 0:
                persons.append(Person(MALE))

                # No more babies.
                stop = True
            else:
                persons.append(Person(FEMALE))

            if stop:
                m.had_boy = True
                f.had_boy = True

        # Increment the age of every person.
        for p in persons:
            p.age += 1

        # Make people die.
        persons = [p for p in persons if p.age < DEATH_AGE]

if __name__ == "__main__":
    main()

