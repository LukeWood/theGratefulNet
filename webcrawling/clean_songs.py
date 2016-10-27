import glob

term_tokens = ["[","Intro","Outro","Verse","(","Interlude"]

def run():
    for fname in glob.glob("songs/*"):
        with open(fname) as f:
            fname = fname.replace("songs/","")
            with open("../data/"+fname,"w") as fo:
                for line in f:
                    line = line.strip()
                    cont = False
                    for term in term_tokens:
                        if(line.startswith(term)):
                            cont = True
                        if line == "":
                            cont = True
                    if cont:
                        continue
                    fo.write(line+'\n')
