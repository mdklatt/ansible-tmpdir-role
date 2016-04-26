tmpdir
======

Create a temporary directory that will be automatically removed.


Role Variables
--------------
- `tmpdir`: root directory to use; default to the system tmp directory
- `template`: template to use for directory name; defaults to tmp.XXXXXXXX

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: tmpdir, root: /tmp, template: tmp.XXXXXXXX }

License
-------

MIT

Author Information
------------------

Michael Klatt 
