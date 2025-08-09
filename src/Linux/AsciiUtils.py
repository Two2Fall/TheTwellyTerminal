"""
AsciiUtils.py           — A python file to create text sections and better ascii documents

This is a python file to create paragraphs and ascii documents better. This
file includes the `TextSection()` class and the pages.
Used modules:
    - rich
"""

from rich.console import Console

AUTHOR = "TwellEvans"
VERSION = 1.0


class TextSection:
    """
    TextSection()         —— A class for text sections

    This class provides methods for text sections in the document, this text
    can be stylized without any problem, because this class use the rich module

    Arguments:
        `Indentation` — The indentation symbol and amount of this document,
        `Console`: — To be better compatible, this class needs a console to render the text section
    Returns: `TextSection()`
    """

    def __init__(self, TabAmount: tuple[str, int], Console: Console) -> None:
        self.Text = []
        self.TabAmount = TabAmount
        self.Console = Console
    def AppendParagraph(self, Paragraph: str):
        """
        TextSection().AppendParagraph()         —— A class for text sections

        This class provides methods for text sections in the document, this text
        can be stylized without any problem, because this class use the rich module

        Arguments:
            `Indentation` — The indentation symbol and amount of this document,
            `Console`: — To be better compatible, this class needs a console to render the text section
        Returns: `TextSection()`
        """
