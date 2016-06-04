""" Test suite for the tmpdir role.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the package is actually
being tested. If the package is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from os import symlink
from os import remove
from os.path import abspath
from os.path import dirname
from os.path import join
from shlex import split
from subprocess import call

import pytest

_ROLE = "tmpdir"


@pytest.yield_fixture(scope="module")
def mklink():
    test_path = dirname(abspath(__file__))
    role_link = join(test_path, _ROLE)
    symlink(dirname(test_path), role_link)
    yield
    remove(role_link)
    return


@pytest.mark.parametrize("variables",
        ({}, {"tmpdir_root": "test"}, {"tmpdir_template": "test.XXXXXX"}))
def test_role(mklink, variables):
    """ Test the role functionality.

    """
    if variables:
        extra = ("=".join(var) for var in variables.iteritems())
        options = "--extra-vars '{:s}'".format(" ".join(extra))
    else:
        options = ""
    cmd = "ansible-playbook {:s} playbook.yml".format(options)
    assert 0 == call(split(cmd), cwd=dirname(abspath(__file__)))

# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))
