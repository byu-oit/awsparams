# usage
use with default profile
`> python params.py ls`

## ls usage
ls names only
`> python params.py ls --profile=trn`

ls with values no decryption
`> python params.py ls --profile=trn --values=True`

ls with values and decryption
`> python params.py ls --profile=trn --values=True --WithDecryption=True`

ls by prefix
`> python params.py ls --prefix=appname.prd`

## new usage
new interactively
`> python params.py new`

new semi-interactively
`> python params.py new appname.prd.username`

new non-interactive
`> python params.py new appname.prd.usrname parameter_value parameter_descripton`

## cp usage
copy a parameter
`> python params cp appname.prd.username newappname.prd.username`

copy set of parameters with prefix appname.dev. to appname.prd.
`> python params.py cp appname.dev. appname.prd. --prefix=True`

copy set of parameters starting with pattern repometa-generator.prd overwrite existing parameters accross different accounts
`> python params.py cp repometa-generator.prd --src_profile=dev --dst_profile=trn --prefix=True`

copy single parameters or list of specific parameters accross different accounts
`> python params.py cp  appname.dev.username appname.trb.username --src_profile=dev --dst_profile=trn`

## mv usage
rename parameters
`> python params.py mv --prefix --profile=[default] repometa-generator.prd repometa-generator.stg # this would rename all parameters with this prefix`
`> python params.py mv --profile=[default] repometa-generator.prd.something repometa-generator.prd.somethingelse # this renames one parameter`