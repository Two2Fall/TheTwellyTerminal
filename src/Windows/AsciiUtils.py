"""
AsciiUtils.py           — A python file to create text sections and better ascii documents

This is a python file to create paragraphs and ascii documents better. This
file includes the `TextSection()` class and the pages.
Used modules:
    - rich
"""

from rich.console import Console

AUTHOR = "TwellEvans"  # Do not change this
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
        self.Paragraphs = []
        self.TabAmount = TabAmount
        self.Console = Console

    def AppendParagraph(self, Paragraph: str):
        """
        `TextSection().AppendParagraph()`         —— A method to append paragraphs

        This method appends a paragraph into the text section, it can have style, so
        you can personalize the text as you want.

        Arguments:
            `Paragraph` — The paragraph to append
        Returns: `None`
        """
        self.Paragraphs.append(Paragraph)

    def RenderAll(self):
        """
        `TextSection().RenderAll()`         —— A method to render the text section

        This method renders the entire text section.

        Arguments: `None`
        Returns: `None`
        """
        for Paragraph in self.Paragraphs:
            self.Console.print(self.TabAmount + Paragraph)

    def GetParagraph(self, ParagraphIndex: int | tuple[int, int]):
        """
        `TextSection().GetParagraph()`      —— A method to get a paragraph by index

        If you need to get a paragraph by index
        use this method.

        Arguments:
            `ParagraphIndex` — The paragraph index
        Returns: `str` or `list`
        """
        if isinstance(ParagraphIndex, tuple):
            return self.Paragraphs[ParagraphIndex[0] : ParagraphIndex[1]]
        elif (
            isinstance(ParagraphIndex, int)
            and ParagraphIndex >= 0
            and ParagraphIndex < len(self.Paragraphs)
        ):
            return self.Paragraphs[ParagraphIndex]

    def RenderPart(self, Indexes: tuple[int, int]):
        """
        `TextSection().RenderPart()`      —— A method to render paragraphs by indexes

        This method is to render a part of the ascii document. This is good if you want to
        import quotes or any important text instead of importing all document

        Arguments:
            `Indexes` — This parameter is for the extracted text document (line by line)
        Returns: `list`
        """
        return self.Paragraphs[Indexes[0] : Indexes[1]]
