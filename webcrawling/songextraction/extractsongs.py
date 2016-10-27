def find_songs(text):
  import re
  matches=re.findall(r'\"(.+?)\"',text)
  # matches is now ['String 1', 'String 2', 'String3']
  return matches

songs = []
for line in open("wikisongs.txt","r"):
    line = line.strip()
    if(len(line) == 1 or len(line) == 0):
        continue
    index = line.rfind("(")
    if(index > -1):
        line = line[:index]
    songs.append(line)

print("\n".join(songs))
