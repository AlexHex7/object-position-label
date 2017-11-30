import os


def make_dir(path, print_info=True):
    if not os.path.exists(path):
        if print_info:
            print('==>Make Dir: %s' % path)
        os.mkdir(path)
