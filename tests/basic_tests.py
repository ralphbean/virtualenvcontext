
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
