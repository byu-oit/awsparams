.. AWSParams documentation master file, created by
   sphinx-quickstart on Wed Jul 25 15:59:06 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AWSParams's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   AwsParams/awsparams
   AwsParams/paramresult


Note
====

Version 1 of this library is drastically different than previous
versions. The CLI Application hasn’t changed but the library it uses
has. Please pay extra attention to the examples below or look at the
underlying class for more information.

Why this script?
================

The current (Jul 2017) AWS Console for the Systems Manager Parameter
Store is good for adding and editing the values of parameters, but
misses key productivity functions like copying (especially en mass),
renaming, etc. The current ``aws ssm`` CLI is very similar in
functionality to the AWS Console.

This script is to automate a lot of the manual work currently needed
with the existing AWS-provided UIs.

Installation
============

-  AWSParams requires Python 3.6+
-  Depending on your Python3.6 install either ``pip install awsparams``
   or ``pip3 install awsparams``

Usage
=====

Library:
--------

.. code:: python

   from awsparams import AWSParams
    
   # Using default Profile
   aws_params = AWSParams()

   # Using a Custome Profile
   aws_params = AWSParams('MyProfile')

   #get a single parameter
   param = get_parameter('test1')
   # ParamResult(Name='test1', Value='test123', Type='SecureString')

   #ParamResult is a named tuple with properties Name, Value, Type
   param.Name # 'test1'
   param.Value # 'test123'
   param.Type # 'SecureString'

   # get multiple parameters with a prefix
   params = get_all_parameters(prefix="testing.testing.")
   # [ParamResult(Name='testing', Value='1234', Type='String'),
   #  ParamResult(Name='testing2', Value='1234', Type='String')]

   # get multiple parameters by path
   params = get_all_parameters(prefix="/testing/testing/", by_path=True)
   # [ParamResult(Name='testing', Value='1234', Type='String'),
   #  ParamResult(Name='testing2', Value='1234', Type='String')]

   # get multiple parameters by path
   params = get_all_parameters(prefix="/testing/testing/", by_path=True, trim_name=False)
   # [ParamResult(Name='/testing/testing/testing', Value='1234', Type='String'),
   #  ParamResult(Name='/testing/testing/testing2', Value='1234', Type='String')]

   # get just a parameter value
   value = get_parameter_value('test1')
   # test123

For more detailed examples of usage as a library see the cli
implementation `here`_.

For full class reference see: :ref:`here <awsparams>`.

CLI application:
----------------

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
================

ls usage
--------

ls names only: ``awsparams ls``

ls with values no decryption: ``awsparams ls --values`` or
``awsparams ls -v``

ls with values and decryption: ``awsparams ls --with-decryption``

ls by prefix: \`awsparams ls appn

.. _here: https://github.com/byu-oit/awsparams/blob/master/awsparams/cli.py


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
