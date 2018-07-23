#!/usr/bin/env python3.6
# Copyright 2016 Brigham Young University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List, NamedTuple, Union

import boto3

__VERSION__ = "1.0.0"


class ParamResult(NamedTuple):
    Name: str
    Value: str
    Type: str


class AWSParams(object):
    ssm = None
    profile = ""

    def __init__(self, profile: str=""):
        self.profile = profile
        if profile:
            session = boto3.Session(profile_name=self.profile)
            self.ssm = session.client("ssm")
        else:
            self.ssm = boto3.client("ssm")

    def _connect_ssm(self, profile: str=""):
        if profile:
            session = boto3.Session(
                profile_name=profile, region_name='us-west-2')
            ssm = session.client("ssm")
        else:
            ssm = boto3.client("ssm")
        return ssm

    def put_parameter(self, parameter: dict, *, overwrite: bool=False, profile: str=""):
        """Put a Parameter"""
        if profile:
            ssm = self._connect_ssm(profile)
        else:
            ssm = self.ssm
        if overwrite:
            parameter["Overwrite"] = True
        ssm.put_parameter(**parameter)

    def remove_parameter(self, param: str):
        """Remove a Parameter"""
        self.ssm.delete_parameter(Name=param)

    def get_parameter_value(self, name: str, *, decryption: bool=False) -> str:
        """Get a Parameter Value"""
        param = self.ssm.get_parameter(Name=name, WithDecryption=decryption)[
            "Parameter"
        ]
        return param["Value"]

    def get_parameter(self, name: str, *, values: bool=False, decryption: bool=False, named_tuple: bool=False) -> Union[dict, ParamResult, None]:
        """Get a Parameter"""
        try:
            param = self.ssm.get_parameter(
                Name=name, WithDecryption=decryption)
        except self.ssm.exceptions.ParameterNotFound:
            return
        result = self.build_param_result(
            param["Parameter"], values=values, named_tuple=named_tuple)
        return result

    def build_param_result(self, param: dict, *, values: bool=False, named_tuple: bool=False) -> Union[dict, ParamResult]:
        """Build a parameter result"""
        result = {
            "Name": param["Name"],
            "Value": param["Value"] if values else None,
            "Type": param["Type"],
        }
        if named_tuple:
            return ParamResult(**result)
        return result

    def get_all_parameters(self, *, prefix: str='', by_path: bool=False, values: bool=False, decryption: bool=False, named_tuple: bool=False) -> Union[List[dict], List[ParamResult]]:
        """Get all parameters Optionally by prefix or path"""
        if by_path:
            path = prefix
        else:
            path = '/'
        parameters = []
        paginator = self.ssm.get_paginator('get_parameters_by_path')
        page_iterator = paginator.paginate(
            Path=path, Recursive=True, WithDecryption=decryption)
        for page in page_iterator:
            if prefix and not by_path:
                parameters.extend(
                    [self.build_param_result(param, values=values, named_tuple=named_tuple)
                     for param in page['Parameters'] if prefix in param['Name']]
                )
            else:
                parameters.extend(
                    [self.build_param_result(param, values=values, named_tuple=named_tuple)
                     for param in page['Parameters']]
                )
        return parameters

    def new_param(self, name: str, value: str, *, param_type: str="String", key: str="", description: str="", overwrite: bool=False):
        """
        Create a new parameter
        """
        param = {
            "Name": name,
            "Value": value,
            "Type": param_type,
            "Overwrite": overwrite,
        }
        if key:
            param['KeyId'] = key
        if description:
            param["Description"] = description
        self.put_parameter(param, overwrite=overwrite)

    def set_param(self, src: str, value: str) -> bool:
        """
        Edit an existing parameter
        """
        existing_value = self.get_parameter_value(src, decryption=True)
        if existing_value != value:
            put = self.get_parameter(
                name=src, values=True, decryption=True
            )
            put["Value"] = value
            self.put_parameter(put, overwrite=True)
            return True
        else:
            return False
