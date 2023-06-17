#!/bin/bash

# change to the modules directory
cd modules

# for each directory in the current directory
for dir in */; do
    # get rid of trailing slash
    dir=${dir%*/}

    # if the directory has a .py file with the same name
    if [[ -f "$dir/$dir.py" ]]; then
        # check if __init__.py already contains an import statement
        if grep -q "from .${dir} import \*" "$dir/__init__.py"; then
            echo "$dir/__init__.py already contains the import statement"
        else
            # add the import statement to __init__.py
            echo "from .${dir} import *" >> "$dir/__init__.py"
            echo "Added import statement to $dir/__init__.py"
        fi
    fi
done

