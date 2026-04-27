# Prog11part1.py
# Author: Austin Carter
# Email: austin.carter.1@und.edu
# Description:
# Part 1 – Ask for a filename, then repeatedly ask for song title and time.
# Stop when a blank title is entered. Write each song to the file separated by a tab.

def main():
    filename = input("Enter data file name: ").strip()

    with open(filename, "w") as outfile:
        while True:
            print('Enter the artist and song, enter "" to quit:')
            title = input("Title: ").strip()

            if title == "":
                break

            time_str = input("Time: ").strip()

            outfile.write(title + "\t" + time_str + "\n")


if __name__ == "__main__":
    main()
