import sys
import random
import string


def randStr():
    return "".join(random.choice(string.ascii_letters) for i in range(10))


def randomize_epy_names(filename):
    with open(filename) as fin:
        contents = fin.read()
        lines = contents.splitlines()

    rawEpys = list(filter(lambda x: "- name: epy_block" in x, lines))
    cleanEpys = list(map(lambda x: x.split(":")[1].strip(), rawEpys))
    ## Assume that only short ones need to be renamed.
    shortEpys = list(filter(lambda x: len(x) < 13, cleanEpys))
    
    modifiedContents = contents
    for epy in shortEpys:
        new = "embpy_" + randStr()
        print("renaming", epy, "to", new)
        modifiedContents = modifiedContents.replace(epy, new)

    if modifiedContents == contents:
        print("No changes.")
        return
        
    with open(filename, "w") as fout:
        fout.write(modifiedContents)


if __name__ == "__main__":
    try: 
        filename = sys.argv[1]
    except IndexError:
        print("Usage: python3 randomize_grc_epy_ids.py filename")
        sys.exit()
    
    if not filename.lower().endswith(".grc"):
        print(f"Can only use on .grc files. Your filename is '{filename}'")
        sys.exit()
    
    print("Note: Ensure that the grc file is closed before running this,")
    print("otherwise the changes will most likely be lost.")
    print("(Specifically, close the file in GNU Radio Companion.)")
    contin = input("Continue? (y|n) ")
    if contin.lower() != "y":
        print("Exiting.")
        sys.exit()
    print("Processing...")
    print()
    randomize_epy_names(filename)
    print("Done.")
    
