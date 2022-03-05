from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)




from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

with managed_resource(timeout=3600) as resource:
    pass
    # Resource is released at the end of this block,
    # even if code in the block raises an exception

