import os
import re
to_dir = "/home/martin/X-Brain/Tianchi"
fname = os.path.join(to_dir, "new_link_info")

def load():
    skip = True
    D = dict()
    with open(fname) as f:
        for line in f:
            if(skip):
                skip = False
                continue
            line = re.sub('\n', '', line)
            info = line.split(";")
            D[info[0]]=(info[1], info[2])
    return D
