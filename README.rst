..  README for the tmpdir-role project.

tmpdir 
======
..  |travis.png| image:: https://travis-ci.org/mdklatt/ansible-tmpdir-role.png?branch=master
    :alt: Travis CI build status
    :target: `travis`_
..  _travis: https://travis-ci.org/mdklatt/ansible-tmpdir-role
..  _Ansible: http://docs.ansible.com/ansible

|travis.png|

`Ansible`_ role to create a temporary working directory that can be used to
store files that will automatically be deleted at the end of the play.


Requirements
------------

Requires the ``mktemp`` command on the target machine.


Role Variables
--------------

Input
+++++
- ``tmpdir_root``: directory root path, which must already exist; defaults to 
  the system tmp directory
- ``template``: template used to create the directory name, where a sequence of
  ``X`` characters is replaced by a unique string; defaults to ``tmp.XXXXXXXX``

Output
++++++
- ``tmpdir_path``: the path to the temporary directory


Example Playbook
----------------

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
