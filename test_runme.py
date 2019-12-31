from runme import exec_in_container
import pytest


def test_exec_in_container_returns_console_output():
    result = exec_in_container('echo "Hello World!"')

    assert 'Hello World!\n' == result


@pytest.mark.parametrize("test_input,expected", [
    ('ip', '/sbin/ip\n'),
    ('hashcat', '/usr/bin/hashcat\n'),
    ('airmon-ng', '/usr/sbin/airmon-ng\n'),
    ('airodump-ng', '/usr/sbin/airodump-ng\n'),
    ('hcxdumptool', '/usr/local/bin/hcxdumptool\n'),
    ('hcxpcaptool', '/usr/local/bin/hcxpcaptool\n')])
def test_container_has_dependencies_installed(test_input, expected):
    result = exec_in_container(f'which {test_input}')

    assert expected == result
