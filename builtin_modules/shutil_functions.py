import shutil

# https://docs.python.org/2/library/shutil.html

src = ""
dst = ""

# move
shutil.move(src, dst)

# copy
shutil.copy(src, dst)

# copy2 also copies metadata 
shutil.copy2(src, dst)

# copy file works faster but it only copies files
shutil.copyfile(src, dst)

# copies metadata
shutil.copystat(src, dst)

# copytree copies entire directories
# for ignoring patters
ignore = shutil.ignore_patterns('*.pyc', 'tmp*')
shutil.copytree(src, dst, ignore=ignore)

# removes entire directorires
shutil.rmtree(src)

# zipdir
shutil.make_archive(dst+".zip", 'zip', src)