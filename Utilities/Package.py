import os
import tempfile
import tarfile
from fnmatch import fnmatch

class Package:
    @classmethod 
    def create(cls, archive_name=None, directories=['.', 'Network', 'Utilities'], filetype='*.py'):
        files = []
        try:
            files = filter(lambda f: fnmatch(f, filetype), reduce(lambda a, d: a + map(lambda f: d + '/' + f, os.listdir(d)), directories, []))
        except OSError:
            # Packaging (obviously) fails on EMR.  Swallow.
            pass

        if archive_name is None: archive_name = tempfile.mktemp() + '.tar.gz'

        tar = tarfile.open(archive_name, "w:gz")
        map(lambda f: tar.add(f), files)
        tar.close()

        return archive_name
