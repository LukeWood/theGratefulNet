def find_songs(text):
  import re
  matches=re.findall(r'\"(.+?)\"',text)
  # matches is now ['String 1', 'String 2', 'String3']
  return matches

# result:
'String 1,String 2,String3'
songs = []
for line in open("wikifile.txt","r"):
    matches = find_songs(line)
    if(matches):
        songs.append("\n".join(matches))

print("\n".join(songs))
