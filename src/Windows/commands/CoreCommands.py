"""
CoreCommands.py       — The core commands into one file

This file contains all the core commands like `clr`, `exit`,
`goto` and more. This file is a module so you can test this as
you want.

Used modules:
    - os
    - typing
"""

import os
from typing import Union, Optional

AUTHOR = "TwellEvans"  # Hey that's me
VERSION = 1.0
COMMANDS = ["clr", "exit", "goto", "ttc", "credits", "repo"]


def ClearScreen():
    """
    This function clears the terminal buffer
    """
    os.system("cls")


def Exit(Code: int):
    """
    Exit()       —— Exit from The Twelly Terminal

    This function makes the program to exit and if it is possible,
    with a code error.

    Arguments: `Code`       —— The output code
    Returns: `NoReturn`
    """
    exit(Code)


def TTCCommand(
    Action: str,
):
    """
    TTCCommand()       —— Play with The Twelly Creations

    With this function, you can use any of The Twelly Creations. This
    function needs arguments, so you have to specify the arguments.

    Arguments:
        `Parameters`
    """
