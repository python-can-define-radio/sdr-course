"""This includes two categories:
- GNU Radio blocks such as the waterfall sink, wrapped to be easier to use
- Hier blocks with a similar purpose
"""

from distutils.version import StrictVersion

from gnuradio import gr
from PyQt5 import Qt
from pcdr.types_and_contracts import top_block_and_widget
from gnuradio import qtgui



def qt_gui_init_boilerplate(tb: top_block_and_widget, classname: str):
    Qt.QWidget.__init__(tb)
    tb.setWindowTitle("Not titled yet")
    qtgui.util.check_set_qss()
    try:
        tb.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
    except:
        pass
    tb.top_scroll_layout = Qt.QVBoxLayout()
    tb.setLayout(tb.top_scroll_layout)
    tb.top_scroll = Qt.QScrollArea()
    tb.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
    tb.top_scroll_layout.addWidget(tb.top_scroll)
    tb.top_scroll.setWidgetResizable(True)
    tb.top_widget = Qt.QWidget()
    tb.top_scroll.setWidget(tb.top_widget)
    tb.top_layout = Qt.QVBoxLayout(tb.top_widget)
    tb.top_grid_layout = Qt.QGridLayout()
    tb.top_layout.addLayout(tb.top_grid_layout)
    tb.settings = Qt.QSettings("GNU Radio", classname)
    try:
        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            tb.restoreGeometry(tb.settings.value("geometry").toByteArray())
        else:
            tb.restoreGeometry(tb.settings.value("geometry"))
    except:
        pass
    

## TODO: Easier waterfall

## TODO: Easier NBFM Receive