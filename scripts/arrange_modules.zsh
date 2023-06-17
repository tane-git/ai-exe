#!/bin/zsh

# For each .py file in the current directory
for file in *.py; do
    # Skip __init__.py file
    if [[ $file == "__init__.py" ]]; then
        continue
    fi

    # Get the filename without extension (which is the module name)
    module="${file%.*}"

    # Create a new directory for the module, if it doesn't exist already
    mkdir -p "$module"

    # Move the .py file into the new directory
    mv "$file" "$module"

    # Create __init__.py file in the new directory
    touch "$module/__init__.py"

    # Create a new test file in the module directory
    touch "$module/test_${module}.py"
done

