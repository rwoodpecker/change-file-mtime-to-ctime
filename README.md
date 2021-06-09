# change-file-mtime-to-ctime
Python script to change the modification time (mtime) of files in a directory to match creation time (ctime).

Run the script through python3 changefilemtimetoctime.py /path/to/directory/. It will only update files in that directory and not recurse. You can specify file types to be ignored in line 19.

If you don't want to specify a directory, move the script to the desired directory and run it with python3 changefilemtimetoctime.py.
