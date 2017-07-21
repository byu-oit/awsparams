Why this script?
================

The current (Jul 2017) AWS Console for the Systems Manager Parameter Store is good for 
adding and editing the values of parameters, but misses key productivity functions like
copying (especially en mass), renaming, etc.  The current ``aws ssm`` CLI is very 
similar in functionality to the AWS Console.

This script is to automate a lot of the manual work currently needed with the existing
AWS-provided UIs.

Usage
=====

ls usage
--------

ls names only

``awsparams ls``

ls with values no decryption

``awsparams ls --values=True``

ls with values and decryption

``awsparams ls --values=True --with-decryption=True``

ls by prefix

``awsparams ls --prefix=appname.prd``

new usage
---------

new interactively

``awsparams new``

new semi-interactively

``awsparams new appname.prd.username``

new non-interactive

``awsparams new appname.prd.usrname parameter_value parameter_descripton``

cp usage
--------

copy a parameter

``awsparams cp appname.prd.username newappname.prd.username``

copy set of parameters with prefix appname.dev. to appname.prd.

``awsparams cp appname.dev. appname.prd. --prefix=True``

copy set of parameters starting with pattern repometa-generator.prd
overwrite existing parameters accross different accounts

``awsparams cp repometa-generator.prd --src_profile=dev --dst_profile=trn --prefix=True``

copy single parameters or list of specific parameters accross different
accounts

``awsparams cp  appname.dev.username appname.trb.username --src_profile=dev --dst_profile=trn``

mv usage
--------

rename/move a parameter

``awsparams mv appname.dev.username appname.prd.username``

rename/move all parameters with a prefix changing only the prefix

``awsparams mv appname.dev appname.prd --prefix=True``