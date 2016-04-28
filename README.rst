..  |travis.png| image:: https://travis-ci.org/mdklatt/ansible-tmpdir-role.png?branch=master
    :alt: Travis CI build status
    :target: `travis`_
..  _travis: https://travis-ci.org/mdklatt/ansible-tmpdir-role

tmpdir |travis.png|
===================

..  _Ansible: http://docs.ansible.com/ansible

Ansible role to create a temporary directory that will be automatically 
removed.


Role Variables
--------------
- ``tmpdir``: root directory to use; default to the system tmp directory
- ``template``: template to use for directory name; defaults to tmp.XXXXXXXX

Example Playbook
----------------

.. code:: YAML

    - hosts: servers
      roles:
        - { role: tmpdir, tmpdir: '/tmp', template: tmp.XXXXXXXX }

License
-------

MIT

Author Information
------------------

Michael Klatt 
