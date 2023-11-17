"""
styledb.py - Loads styles from the flatland database common to all Presentations
"""
import logging
from pathlib import Path
import yaml
from collections import namedtuple

_logger = logging.getLogger(__name__)

Float_RGB = namedtuple('Float_RGB', 'R G B')
Line_Style = namedtuple('Line_Style', 'pattern width color')
Text_Style = namedtuple('Text_Style', 'typeface size slant weight color spacing')
Dash_Pattern = namedtuple('Dash_Pattern', 'solid blank')

# Configuration files
colors_path = Path(__file__).parent / "colors.yaml"


class StyleDB:
    """
    Singleton class interface to the Presentation and Styles in the Flatland database. Created with an initial
    Presentation and loads all presentation/style data for that Presentation for easy access by
    the Tabletx.
    """
    rgbF = {}  # rgb color float representation
    # dash_pattern = {}
    # line_style = {}
    # typeface = {}
    # text_style = {}
    # color_usage = {}

    @classmethod
    def load_colors(cls):
        """
        Load all colors from the system colors yaml file

        :return:
        """
        color_text = colors_path.read_text()
        colors = yaml.safe_load(color_text)
        for name, rgb in colors.items():
            StyleDB.rgbF[name] = Float_RGB(R=round(rgb['R'] / 255, 2),
                                           G=round(rgb['G'] / 255, 2),
                                           B=round(rgb['B'] / 255, 2))

    @classmethod
    def report_colors(cls):
        cls.load_colors()
        print("Canvas colors:")
        print("---")
        for c in cls.rgbF:
            print(c)
        print("===")
