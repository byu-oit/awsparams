# Usage

## ls usage
ls names only

`python awsparams.py ls`

ls with values no decryption

`python awsparams.py ls --values=True`

ls with values and decryption

`python awsparams.py ls --values=True --with-decryption=True`

ls by prefix

`python awsparams.py ls --prefix=appname.prd`

## new usage
new interactively

`python awsparams.py new`

new semi-interactively

`python awsparams.py new appname.prd.username`

new non-interactive

`python awsparams.py new appname.prd.usrname parameter_value parameter_descripton`

## cp usage
copy a parameter

`python awsparams.py cp appname.prd.username newappname.prd.username`

copy set of parameters with prefix appname.dev. to appname.prd.

`python awsparams.py cp appname.dev. appname.prd. --prefix=True`

copy set of parameters starting with pattern repometa-generator.prd overwrite existing parameters accross different accounts

`python awsparams.py cp repometa-generator.prd --src_profile=dev --dst_profile=trn --prefix=True`

copy single parameters or list of specific parameters accross different accounts

`python awsparams.py cp  appname.dev.username appname.trb.username --src_profile=dev --dst_profile=trn`

## mv usage
rename/move a parameter

`python awsparams.py mv appname.dev.username appname.prd.username`

rename/move all parameters with a prefix changing only the prefix

`python awsparams.py mv appname.dev appname.prd --prefix=True`