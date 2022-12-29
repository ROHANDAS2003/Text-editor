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

        redo_action = QAction(QIcon('redo.png'),'redo', self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        tool_bar.addSeparator()

        cut_action = QAction(QIcon('cut.png'), 'cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        copy_action = QAction(QIcon('copy.png'), 'copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)
        
        paste_action = QAction(QIcon('paste.png'), 'paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        ToolBar.addSeparator()

        bold_action = QAction(QIcon("bold.png"), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        ToolBar.addAction(bold_action)
        self.addToolBar(tool_bar)


app = QApplication(sys.argv)
window = TextEditor()
window.show()
sys.exit(app.exec_ ())
