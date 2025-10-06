import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tapas import add_bar, tapas_bars


def test_add_bar():
    tapas_bars.clear()
    result = add_bar("Bar Granada", "Granada")
    assert result == True
    assert len(tapas_bars) == 1
    bar = tapas_bars[0]
    assert bar["name"] == "Bar Granada"
    assert bar["city"] == "Granada"