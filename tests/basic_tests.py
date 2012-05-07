# Copyright (C) 2011-2012 Ralph Bean
# License: http://www.gnu.org/licenses/gpl-2.0.txt GPL version 2 or higher

TEST_VENV = 'test_virtualenv_package'


def _do_virtualenv_command(cmd):
    import subprocess
    out, err = subprocess.Popen(
        ['bash', '-c', '. /usr/bin/virtualenvwrapper.sh; %s' % cmd],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).communicate()
    print out
    print err


def setup():
    _do_virtualenv_command('mkvirtualenv --no-site-packages ' + TEST_VENV)


def teardown():
    _do_virtualenv_command('rmvirtualenv ' + TEST_VENV)


def test_gzip():
    import virtualenvcontext as vc
    with vc.VirtualenvContext(TEST_VENV):
        import gzip
