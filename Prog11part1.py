# Prog11part1.py
# Author: Austin Carter
# Email: austin.carter.1@und.edu
# Description:
# Part 1 – Ask for a filename, then ask for a list of songs.
# Each song has a title and a time in minutes:seconds format.
# Write each song to the file with fields separated by a tab.

def main():
    filename = input("Enter data file name: ").strip()

    with open(filename, "w") as outfile:
        while True:
            print('Enter the artist and song, enter "" to quit:')
            title = input("Title: ").strip()

            if title == "":
                break

            time_str = input("Time: ").strip()

            # Write one line: title <tab> time
            outfile.write(title + "\t" + time_str + "\n")


if __name__ == "__main__":
    main()
