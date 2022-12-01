
"""
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Write a Python program to find the Elf carrying the most Calories. How many total Calories is that Elf carrying?



"""

# Function to read in the file and return a list of the lines
def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

# Function to find the Elf carrying the most Calories
def find_elf(lines):
    # Initialize variables
    elf_calories = 0
    elf_number = 0
    elf_calories_max = 0
    elf_number_max = 0
    # Loop through the lines
    for i in range(len(lines)):
        # If the line is blank, then we have a new Elf
        if lines[i] == '\n':
            # If the current Elf has more Calories than the previous Elf, then update the max
            if elf_calories > elf_calories_max:
                elf_calories_max = elf_calories
                elf_number_max = elf_number
            # Reset the current Elf's Calories
            elf_calories = 0
            # Increment the Elf number
            elf_number += 1
        # If the line is not blank, then add the Calories to the current Elf's Calories
        else:
            elf_calories += int(lines[i])
    # Return the Elf number and the Calories
    return elf_number_max, elf_calories_max

# Main function
def main():
    # Read in the file
    lines = read_file('calories.txt')
    # Find the Elf carrying the most Calories
    elf_number, elf_calories = find_elf(lines)
    # Print the results
    print('Elf {} is carrying the most Calories: {}'.format(elf_number, elf_calories))

# Run the program
if __name__ == '__main__':
    main()
