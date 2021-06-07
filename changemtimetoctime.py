import os
import platform
import sys

def ctime(file): # to return c time of files.
    if platform.system() == 'Windows':
        return os.path.getctime(file)
    else:
        stat = os.stat(file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # Can't get file creation time on linux.
            sys.exit("No creation time could be found. You are using a system that doesn't support ctimes. Exiting.")

def mtime(file):  # to return m time of files.
    return os.stat(file).st_mtime

ignores = [".py", ".DS_Store"] # ignore files that we don't want to update.
filenames = next(os.walk(os.getcwd()))[2] # Only get files, not directories.

for filename in filenames:
    if not filename.endswith(tuple(ignores)):
        if mtime(filename) == ctime(filename): 
            print(f"Not updating - mtime is already the same as ctime for: {filename}.")
        else:
            print(f"Changing the mtime of file: {filename} from {mtime(filename)} to {ctime(filename)}")
            os.utime(filename, (ctime(filename), ctime(filename))) #change accessed and mtime to file ctime
