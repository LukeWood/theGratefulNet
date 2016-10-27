from Song import Song

def run():
    for line in open("songextraction/songs.txt"):
        line = line.strip()
        song = Song(artist="Grateful Dead", title=line)
        lyr = song.lyricwikia()
        if lyr is not None:
            with open("songs/"+line.replace("\n","")+".txt","w") as f:
                f.write(lyr)
