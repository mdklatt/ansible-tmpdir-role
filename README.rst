..  README for the tmpdir Ansible role.

======
tmpdir 
======
..  |travis.png| image:: https://travis-ci.org/mdklatt/ansible-tmpdir-role.png?branch=master
    :alt: Travis CI build status
    :target: `travis`_
..  _travis: https://travis-ci.org/mdklatt/ansible-tmpdir-role
..  _Ansible: http://docs.ansible.com/ansible

|travis.png|

This `Ansible`_ role will create a temporary working directory that will be
automatically deleted at the end of the play. Only one directory is created
per play regardless of the number of times this role is included.


Requirements
============
Requires the ``mktemp`` command on the target machine.


Role Variables
==============
- ``tmpdir_root``: root path (must exist); defaults to system tmp directory
- ``tmpdir_template``: used to create directory name; defaults to ``tmp.XXXXXX``
- ``tmpdir_path``: directory path; created at runtime

The ``root`` and ``template`` variables should only be set at the playbook
level. Once the temporary directory is created, changes to these variables will
have no effect. Thus, other roles that use this role should not depend on being
able to modify these values for their own use.


Available Tags
==============
- ``debug``: show debugging output


Example Playbook
================
..  code::

    - hosts: all
      
      roles:
      - role: tmpdir
        tmpdir_root: '/tmp'
        tmpdir_template: tmp.XXXXXXXX
        tmpdir_debug: True
      
      tasks:
      - name: download tmpdir source
        unarchive:
          src: "https://github.com/mdklatt/ansible-tmpdir-role/archive/master.zip"
          dest: "{{ tmpdir_path }}"
          copy: False
