""" Test the tmpdir role.

For now, this checks the syntax. No functionality is tested.

"""
from contextlib import contextmanager
from os import chdir
from os import getcwd
from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from shlex import split
from shutil import copytree
from shutil import rmtree
from subprocess import check_call
from tempfile import mkdtemp


_ROLE = "tmpdir"


def main():
    """ Run tests.
    
    """
    # TODO: Need to verify that the role is installable via `ansible-galaxy`.
    # The meta/main.yml file contains a 'galaxy_info' directory that needs to
    # be valid for the role to be installed from a git repo.

    @contextmanager
    def tmpdir():
        """ Enter a self-deleting temporary directory. """
        cwd = getcwd()
        tmp = mkdtemp()
        try:
            chdir(tmp)
            yield tmp
        finally:
            rmtree(tmp)
            chdir(cwd)
        return
    
    def install():
        """ Install the role in the current directory. """
        dirs = "defaults", "handlers", "meta", "tasks", "tests"
        for name in dirs:
            copytree(join(origin, name), join(_ROLE, name))
        return

    origin = dirname(dirname(abspath(__file__)))
    print(origin)
    with tmpdir() as tmp:
        root = join(tmp, _ROLE)
        install()
        ansible = "ansible-playbook --syntax-check -i inventory test.yml"
        check_call(split(ansible), cwd=join(root, "tests"))
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
