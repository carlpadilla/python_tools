#    Usage: del_empty_dir.py \"E:/folder path here\

import os
import sys
import shutil
import time

path = sys.argv[1]


def move_up_dir():
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            try:
                print(file)
                shutil.move(os.path.join(root, file), path)
                os.remove(file)
            # os.rmdir()
            except OSError:
                pass


def del_empty_dir():
    if len(sys.argv) == 1:
        # Print usage
        print("Usage: del_empty_dir.py \"E:/folder path here\"")
    else:
        for root, dirs, files in os.walk(path, topdown=False):
            for name in dirs:
                try:
                    if len(os.listdir(os.path.join(root, name))) == 0:  # check whether the directory is empty
                        print("Deleting", os.path.join(root, name))
                        try:
                            os.rmdir(os.path.join(root, name))
                        except:
                            print("FAILED :", os.path.join(root, name))
                            pass
                except:
                    pass


move_up_dir()
time.sleep(5)
del_empty_dir()