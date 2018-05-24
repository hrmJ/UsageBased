"""

Process the concordances from syntactically annotated data in order to use
in R

"""
#!/usr/bin/python3
import sys
import re
import glob
import json
import os

def Process(fname):
    """
    Process one file
    """
    pat =  re.compile(r"\d+\t\?[^\n]+\n\n?"*9 + r"\d+\t\?[^\n]+\n\n")
    with open(fname, "r") as f:
        contents = f.read()
    splitted = pat.split(contents)
    #remove empty segments
    splitted = [sp for sp in splitted if sp]
    return {
            os.path.basename(fname).replace(".txt.prepared.conll",""):splitted
           }


if __name__ == "__main__":
    #Process(sys.argv[1])
    all_data = []
    try:
        if os.path.isdir(sys.argv[1]):
            for f in glob.glob(sys.argv[1] + "/*"):
                print("Processing " + f)
                all_data.append(Process(f))
            with open("results.json","w") as f:
                json.dump(all_data,f,ensure_ascii=False,indent=4)
        else:
            Process(f)
    except IndexError:
        print("Usage:" + sys.argv[0] + "<folder or file>")

