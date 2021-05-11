# Used to generate JSON Validations chema for requirements.
import sys
from typing import Any, List, Mapping, Optional

from pydantic import BaseModel, Extra, Field

from . import consts

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal


class MoleculeDriverOptionsModel(BaseModel):
    managed: Optional[bool]
    login_cmd_template: Optional[str]
    ansible_connection_options: Optional[Mapping[str, str]]

    class Config:
        extra = Extra.forbid


class MoleculeDriverModel(BaseModel):
    # https://github.com/ansible-community/toolset/blob/main/requirements.in
    name: Optional[
        Literal[
            "azure",
            "ec2",
            "delegated",
            "docker",
            "containers",
            "openstack",
            "podman",
            "vagrant",
            "digitalocean",
            "gce",
            "libvirt",
            "lxd",
        ]
    ]
    options: Optional[MoleculeDriverOptionsModel]

    class Config:
        extra = Extra.forbid


class ContainerRegistryModel(BaseModel):
    url: str

    class Config:
        extra = Extra.forbid


class MoleculePlatformModel(BaseModel):
    name: str
    hostname: Optional[str]
    environment: Optional[Mapping[str, str]]
    # container specific
    image: Optional[str]
    registry: Optional[ContainerRegistryModel]
    dockerfile: Optional[str]
    volumes: Optional[List[str]]
    privileged: Optional[bool]
    ulimits: Optional[List[str]]
    # other
    pkg_extras: Optional[str]

    class Config:
        extra = Extra.forbid


class ProvisionerConfigOptionsModel(BaseModel):
    class ProvisionerConfigOptionsDefaultsModel(BaseModel):
        ansible_managed: Optional[str] = Field(
            default="Ansible managed: Do NOT edit this file manually!"
        )
        display_failed_stderr: Optional[bool] = Field(default=True)
        fact_caching: Optional[str]
        fact_caching_connection: Optional[str]
        forks: Optional[int] = Field(default=50)
        host_key_checking: Optional[bool] = Field(default=False)
        interpreter_python: Optional[str] = Field(
            default="auto_silent",
            description="See https://docs.ansible.com/ansible/devel/reference_appendices/interpreter_discovery.html",
        )
        nocows: Optional[int] = Field(default=1)
        retry_files_enabled: Optional[bool] = Field(default=False)

        class Config:
            extra = Extra.forbid

    class ProvisionerConfigOptionsSshConnectionModel(BaseModel):
        control_path: Optional[str] = Field(default="%(directory)s/%%h-%%p-%%r")
        scp_if_ssh: Optional[bool] = Field(default=True)

        class Config:
            extra = Extra.forbid

    defaults: Optional[ProvisionerConfigOptionsDefaultsModel]
    ssh_connection: Optional[ProvisionerConfigOptionsSshConnectionModel]

    class Config:
        extra = Extra.forbid


class ProvisionerModel(BaseModel):
    name: Optional[Literal["ansible"]]
    log: Optional[bool]
    env: Optional[Mapping[str, Any]]
    inventory: Optional[Mapping[str, Any]]
    config_options: Optional[ProvisionerConfigOptionsModel]

    class Config:
        extra = Extra.forbid


class VerifierModel(BaseModel):
    # https://github.com/ansible-community/toolset/blob/main/requirements.in
    name: Optional[Literal["ansible", "goss", "inspec", "testinfra"]] = Field(
        default="ansible"
    )

    class Config:
        extra = Extra.forbid


class MoleculeScenarioModel(BaseModel):
    log: Optional[bool] = Field(default=True)
    driver: MoleculeDriverModel
    platforms: List[MoleculePlatformModel]
    provisioner: Optional[ProvisionerModel]
    scenario: Mapping[
        Literal[
            "check_sequence",
            "cleanup_sequence",
            "converge_sequence",
            "create_sequence",
            "dependency_sequence",
            "destroy_sequence",
            "idempotence_sequence",
            "lint_sequence",
            "prepare_sequence",
            "side_effect_sequence",
            "syntax_sequence",
            "test_sequence",
            "verify_sequence",
        ],
        List[
            Literal[
                "check",
                "cleanup",
                "converge",
                "create",
                "dependency",
                "destroy",
                "idempotence",
                "lint",
                "prepare",
                "side_effect",
                "syntax",
                "test",
                "verify",
            ]
        ],
    ]
    verifier: Optional[VerifierModel]

    class Config:
        extra = Extra.forbid
        title = "Molecule Scenario Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
            "examples": ["molecule/*/molecule.yml"],
        }
