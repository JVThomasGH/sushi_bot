import glob
import os


def clean_folder():
    files = glob.glob('C:\\Learning\\GameBot\\Images\\*')
    for f in files:
        os.remove(f)

clean_folder()