""" make_a_tablet.py - For testing the successful creation of a tabletlib on the command line """

from pathlib import Path
from tabletlib.tablet import Tablet
from tabletlib.geometry_types import Rect_Size

def tabloid_size_tablet() -> Tablet:
    size = Rect_Size(11*72, 17*72)  # 11x17 in points
    output_path = Path(__file__).parent.parent.parent / "working" / "output.pdf"
    return Tablet(size=size, output_file=output_path, drawing_type="xUML state machine diagram", presentation="default",
                  layer="diagram")