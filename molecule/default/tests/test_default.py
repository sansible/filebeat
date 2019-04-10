import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package,version', [
    ('filebeat', '6.6.1'),
])
def test_installed_apt_packages(host, package, version):
    assert host.package(package).is_installed
    assert version in host.package(package).version


@pytest.mark.parametrize('filename', [
    ('/etc/filebeat/filebeat.yml'),
])
def test_config_files(host, filename):
    with host.sudo():
        assert host.file(filename).is_file


def test_hosts_file(host):
    # Assert /etc/hosts exists,...
    f = host.file('/etc/hosts')
    assert f.exists
    # ...is owned by the user root,...
    assert f.user == 'root'
    # ...and owned by the group root.
    assert f.group == 'root'

# See http://testinfra.readthedocs.io/ for guidance on writing testinfra tests.
