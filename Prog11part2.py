# Prog11part2.py
# Author: Austin Carter
# Email: austin.carter.1@und.edu
# Description:
# Part 2 – Functions for processing song/time information.

def timeToSecs(time):
    parts = time.split(":")
    minutes = int(parts[0])
    seconds = int(parts[1])
    return minutes * 60 + seconds


def secsToTime(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    if secs < 10:
        return str(minutes) + ":0" + str(secs)
    return str(minutes) + ":" + str(secs)


def readSongs(fileName):
    musicInfo = {}
    with open(fileName, "r") as infile:
        for line in infile:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("\t")
            song = parts[0]
            time = parts[1]
            musicInfo[song] = time
    return musicInfo


def totalSongs(musicInfo):
    count = 0
    for _ in musicInfo:
        count += 1
    return count


def updateSong(musicInfo, songToFind, newTime):
    if songToFind in musicInfo:
        musicInfo[songToFind] = newTime
        return True
    return False


def totalTime(musicInfo):
    total_seconds = 0
    for song in musicInfo:
        total_seconds += timeToSecs(musicInfo[song])
    return secsToTime(total_seconds)


def findShortestSong(musicInfo):
    first = True
    shortest_song = ""
    shortest_time = 0

    for song in musicInfo:
        secs = timeToSecs(musicInfo[song])
        if first or secs < shortest_time:
            shortest_time = secs
            shortest_song = song
            first = False

    return shortest_song


def findLongestSong(musicInfo):
    first = True
    longest_song = ""
    longest_time = 0

    for song in musicInfo:
        secs = timeToSecs(musicInfo[song])
        if first or secs > longest_time:
            longest_time = secs
            longest_song = song
            first = False

    return longest_song


def getSongTime(musicInfo, songToFind):
    if songToFind in musicInfo:
        return musicInfo[songToFind]
    return ""


def printMusic(title, musicInfo):
    print(title)
    print("Song                          Time")

    # DO NOT SORT — grader requires original order
    for song in musicInfo:
        time = musicInfo[song]
        print(f"{song:<30}{time:>7}")


def matchingSongsByText(musicInfo, textToFind):
    result = []
    text_lower = textToFind.lower()

    for song in musicInfo:
        if text_lower in song.lower():
            result.append(song)

    return result


# main() MUST NOT RUN in Gradescope
if __name__ == "__main__":
    pass

