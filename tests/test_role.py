""" Test the tmpdir role.

"""
from argparse import ArgumentParser
from contextlib import contextmanager
from os import chdir
from os import getcwd
from os.path import abspath
from os.path import dirname
from os.path import join
from shlex import split
from shutil import copytree
from shutil import rmtree
from subprocess import check_call
from tempfile import mkdtemp


_ROLE = "tmpdir"


def _cmdline(argv=None):
    """ Parse command line arguments.
    
    By default, sys.argv is parsed.
    
    """
    parser = ArgumentParser()
    parser.add_argument("--syntax", action="store_true",
                        help="syntax check only")
    return parser.parse_args(argv)


def main(argv=None):
    """ Run tests.
    
    This will install the role to a temporary directory and verify that the
    role correctly creates and removes a (different) temporary directory.
    
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

    def ansible():
        """ Run ansible-playbook. """
        # Make sure to run Ansible with tests/ as the working directory so that
        # tests/ansible.cfg is used.
        extra = " ".join("=".join(var) for var in variables.iteritems())
        if extra:
            options.append("--extra-vars '{:s}'".format(extra))
        cmd = "ansible-playbook {:s} playbook.yml".format(" ".join(options))
        check_call(split(cmd), cwd=join(root ,"tests"))
        return

    args = _cmdline(argv)
    origin = dirname(dirname(abspath(__file__)))
    with tmpdir() as tmp:
        root = join(tmp, _ROLE)
        install()
        options = []
        if args.syntax:
            options.append("--syntax-check")
        variables = {}
        ansible()
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
