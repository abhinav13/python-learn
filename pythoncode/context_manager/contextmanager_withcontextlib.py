from contextlb import contextmanager


@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("Error detected ")
        f_obj.close()


if __name__ == '__main__':
    with file_open('/tmp/file3.txt') as f:
        f.write('Testing is complete')
