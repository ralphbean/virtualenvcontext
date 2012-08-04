# Copyright (C) 2011-2012 Ralph Bean
# License: http://www.gnu.org/licenses/gpl-2.0.txt GPL version 2 or higher

import os
import subprocess
import sys

from nose.tools import raises


def install_distributions(distributions):
    """ Installs distributions with pip! """

    pipsecutable = os.path.sep.join(
        sys.executable.split(os.path.sep)[:-1] + ['pip'])
    cmd = '%s install %s' % (pipsecutable, ' '.join(distributions))
    status = subprocess.call(cmd, shell=True)

TEST_VENV = 'test_virtualenv_package'


def _do_virtualenv_command(cmd):
    out, err = subprocess.Popen(
        ['bash', '-c', '. /usr/bin/virtualenvwrapper.sh; %s' % cmd],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).communicate()
    print out
    print err


def setup():
    version = "%i.%i" % (sys.version_info[0], sys.version_info[1])
    executable = "python%s" % version
    _do_virtualenv_command(
        'mkvirtualenv --no-site-packages --python=%s %s' % (
            executable, TEST_VENV)
    )


def teardown():
    _do_virtualenv_command('rmvirtualenv ' + TEST_VENV)


@raises(ImportError)
def test_no_global_mattd():
    import mattd


@raises(ImportError)
def test_no_venv_mattd():
    import virtualenvcontext as vc
    with vc.VirtualenvContext(TEST_VENV):
        import mattd


def test_install_into_virtualenv():
    import virtualenvcontext as vc
    with vc.VirtualenvContext(TEST_VENV):
        install_distributions(['mattd'])
        import mattd
