from pathlib import Path

# To get the home directory of the current user
print(Path.home())

# make dirs (this is superior dir creating method)
# Path("path").mkdir(parents=True, exist_ok=True) 


# Setup a path first
path = Path("00-modules/builtin_modules/pathlib_examples.py")
print(path)
print(path.absolute())

print(path.exists())
print(path.is_file())
print(path.is_dir())


# extension of the file
print(path.suffix)  

# without the suffix
print(path.stem)

# The parent of the file
print(path.parent)


