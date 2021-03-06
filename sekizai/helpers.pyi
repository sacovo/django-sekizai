# -*- coding: utf-8 -*-
from typing import Dict, List, Union

from django.template.base import Context, Node, NodeList, Template


def _get_nodelist(tpl: Template) -> NodeList: ...

def is_variable_extend_node(node: Node) -> bool: ...

def get_context() -> Context: ...

def _extend_blocks(extend_node: Node, blocks: Dict[str, Node]): ...

def _extend_nodelist(extend_node: Node) -> List[str]: ...

def _scan_namespaces(nodelist: NodeList, current_block: Union[None, Node]) -> List[str]: ...

def get_namespaces(template: str) -> List[str]: ...

def validate_template(template: str, namespaces: List[str]) -> bool: ...

def get_varname() -> str: ...

class Watcher:
    def __init__(self, context: Context) -> None: ...

    @property
    def data(self) -> dict: ...

    def get_changes(self) -> dict: ...
