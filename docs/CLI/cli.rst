.. _cli:

CLI application
================

Usage can be referenced by running ``awsparams --help`` or
``awsparams subcommand --help`` commands:

::

   Usage: awsparams [OPTIONS] COMMAND [ARGS]...

   Options:
   --version  Show the version and exit.
   --help     Show this message and exit.

   Commands:
   cp   Copy a parameter, optionally across accounts
   ls   List Paramters, optional matching a specific...
   mv   Move or rename a parameter
   new  Create a new parameter
   rm   Remove/Delete a parameter
   set  Edit an existing parameter


Command Examples
----------------

ls usage
--------

ls names only: ``awsparams ls``

ls with values no decryption: ``awsparams ls --values`` or
``awsparams ls -v``

ls with values and decryption: ``awsparams ls --with-decryption``

ls by prefix: ``awsparams ls appname.prd``

ls with values, formatted as an environment variable string: ``awsparams ls -v --env-format <prefix>`` or ``awsparams ls -v -f <prefix>``
*`--env-format`/`-f` is used for easy quickly pasting into run configurations in IDE's*

new usage
---------

new interactively: ``awsparams new``

new semi-interactively: ``awsparams new --name appname.prd.username``

new non-interactive:
``awsparams new --name appname.prd.usrname --value parameter_value --description parameter_descripton``

cp usage
--------

copy a parameter:
``awsparams cp appname.prd.username newappname.prd.username``

copy set of parameters with prefix appname.dev. to appname.prd.:
``awsparams cp appname.dev. appname.prd. --prefix``

copy set of parameters starting with prefix repometa-generator.prd
overwrite existing parameters accross different accounts:
``awsparams cp repometa-generator.prd --src_profile=dev --dst_profile=trn --prefix=True``

copy single parameters accross different accounts:
``awsparams cp appname.dev.username appname.trb.us``
