from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import docx2txt
import sys


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(20)
        self.showMaximized()
        self.setWindowTitle('Text Editor')
        self.create_tool_bar()

    def create_tool_bar(self):
        tool_bar = QToolBar("Tools", self)

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

        tool_bar.addSeparator()

        bold_action = QAction(QIcon("bold.png"), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        tool_bar.addAction(bold_action)

        underline_action = QAction(QIcon("underline.png"), 'Underline', self)
        underline_action.triggered.connect(self.underline_text)
        tool_bar.addAction(underline_action)

        italic_action = QAction(QIcon("italic.png"), 'Italic', self)
        italic_action.triggered.connect(self.italic_text)
        tool_bar.addAction(italic_action)

        tool_bar.addSeparator()

        right_alignment_action = QAction(QIcon("right-align.png"), 'Align Right', self)
        right_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
        tool_bar.addAction(right_alignment_action)

        left_alignment_action = QAction(QIcon("left-align.png"), 'Align Left', self)
        left_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
        tool_bar.addAction(left_alignment_action)

        justification_action = QAction(QIcon("justification.png"), 'Center/Justify', self)
        justification_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
        tool_bar.addAction(justification_action)

        self.addToolBar(tool_bar)


    def italic_text(self):
        # if already italic, change into normal, else italic
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    def underline_text(self):
        # if already underlined, change into normal, else underlined
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

    def bold_text(self):
        # if already bold, make normal, else make bold
        if self.editor.fontWeight() != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)


app = QApplication(sys.argv)
window = TextEditor()
window.show()
sys.exit(app.exec_ ())
