from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class TextEditor(QMainWindow):
    def __init__(self) -> None:
        super(TextEditor, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(20)
        self.showMaximized()
        self.setWindowTitle('Text Editor')
        self.create_tool_bar()

    def create_tool_bar(self):
        tool_bar = QToolBar()

        undo_action = QAction(QIcon('undo.png'),'undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        self.addToolBar(tool_bar)


app = QApplication(sys.argv)
window = TextEditor()
window.show()
sys.exit(app.exec_ ())
