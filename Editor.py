from PyQt5.QtWidgets import *
import sys


class TextEditor(QMainWindow):
    def __init__(self) -> None:
        super(TextEditor, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(20)
        self.showMaximized()
        self.setWindowTitle('Text Editor')
app = QApplication(sys.argv)
window = TextEditor()
window.show()
sys.exit(app.exec_ ())
