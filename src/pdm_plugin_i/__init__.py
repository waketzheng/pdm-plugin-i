"""
pdm-plugin-i

A PDM plugin that support `pdm i` as alias of `pdm install`
:author: Waket Zheng <waketzheng@gmail.com>
:license: MIT
"""

from pdm.core import Core

from .command import Command


def plugin(core: Core) -> None:
    core.register_command(Command)
