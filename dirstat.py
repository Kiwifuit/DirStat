from sys import argv
from glob import iglob
from os import chdir, path, sep
from tabulate import tabulate

if len(argv) == 1:
    raise SystemExit("! No path Specified")
    # Walrus operator (:=) to assign variables on conditionals.
    # Very neat feature if I were to say so myself
    # Also the variable becomes a global in this instance...
elif path.isdir((searchPath := path.abspath(argv[1]).replace(sep, "/"))):
    print(f" * Changing directory to {searchPath!r}")
    chdir(searchPath)
    print(
        " * Listing Directories. This might take a while if the folder contains a lot of files"
    )

    fileExtensions = {}

    # I'm gonna add a sorting feature so that's what this variable is for
    # Might change it
    noext = 0
    dirSize = 0
    modifier = "Bytes"

    # Using "iglob()" instead of the normal "glob()" to reduce
    # Waiting time since "iglob()" is a generator
    for file in iglob("**", recursive=True):
        if path.isfile(file):
            dirSize += path.getsize(file)
            file = file.split(sep)[-1].split(".")
            if len(file) == 1:
                # fileExtensions["No Extension"] += 1
                noext += 1
            else:
                # This could be optimized, not sure how
                # It's just my intuition
                fileExtensions[f"*.{file[-1]}"] = (
                    fileExtensions[f"*.{file[-1]}"] + 1
                    if f"*.{file[-1]}" in fileExtensions.keys()
                    else 1
                )
    if len(str(dirSize)) >= 10:
        dirSize = round(dirSize / 1073741824, 2)
        modifier = "Gigabytes"
    fileExtensions = dict(sorted(fileExtensions.items(), key=lambda item: item[0]))
    # Might remove this. I dunno
    fileExtensions.update(
        {
            "All Files": sum(fileExtensions.values()),
            "No Extension": noext,
            "Directory Size": str(dirSize) + f" {modifier}",
        }
    )
    print(
        tabulate(
            [[name, count] for name, count in fileExtensions.items()],
            headers=["Extension", "Frequency"],
            showindex=True,
            tablefmt="orgtbl",
        )
    )

else:
    # ...so it can be used here!
    raise SystemExit(f" ! {searchPath!r} is not a valid path")
