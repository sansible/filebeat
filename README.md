# Elastic Filebeat

Master: [![Build Status](https://travis-ci.org/sansible/filebeat.svg?branch=master)](https://travis-ci.org/sansible/filebeat)
Develop: [![Build Status](https://travis-ci.org/sansible/filebeat.svg?branch=develop)](https://travis-ci.org/sansible/filebeat)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role ...


## Installation and Dependencies

To install run `ansible-galaxy install sansible.filebeat` or add this to your
`roles.yml`.

```YAML
- name: sansible.filebeat
  version: v1.0.0-latest
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses tags: **build** and **configure**

* `build` - Installs Filebeat
* `configure` - Configures Filebeat


## Examples

Simply include role in your playbook with configuration

```YAML
- name: Install and Configure filebeat
  hosts: somehost

  roles:
    - role: sansible.filebeat
      sansible_filebeat_configuration:
        filebeat.inputs:
          - type: log
            enabled: true
            json.keys_under_root: true
        output.elasticsearch:
          hosts:
            - localhost:9200
          index: "test-%{+yyyy.MM.dd}"
        setup.template:
          name: test
          pattern: test-*
          enabled: false
```
