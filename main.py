import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QListWidget, QListWidgetItem, QWidget, QGroupBox, QPushButton)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Host the Test Case list component and the Test Case setting component
        upper_layout = QHBoxLayout()
        test_case_component_assembled = self.create_test_case_component()
        test_case_setting_component_assembled = self.create_test_case_setting_component()

        # Create the Test Case Settings Component Layout then add it to the main layout

        self.setLayout(main_layout)
        self.show()

    def create_test_case_component(self):
        test_case_component_layout = QVBoxLayout()

        # Create labels for each part of the list displayed
        header = self.test_case_header()
        test_case_component_layout.addLayout(header)

        # Create a list that displays the Test Cases saved
        test_case_list = self.test_case_list()
        test_case_component_layout.addLayout(test_case_list)

        # Create the buttons new, edit and delete for the Test Cases
        test_case_btns = self.test_case_btns()
        test_case_component_layout.addLayout(test_case_btns)

        return test_case_component_layout

    def test_case_btns(self):
        btn_layout = QHBoxLayout()

        # Create the buttons
        new_btn = QPushButton('New')
        edit_btn = QPushButton('Edit')
        del_btn = QPushButton('Delete')
        # Add the buttons to the layout
        btn_layout.addWidget(new_btn)
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(del_btn)

        return btn_layout

    def test_case_header(self):
        header_layout = QHBoxLayout()

        #Create the label for the Test Cases list
        lbl1 = QLabel('Test Cases')
        header_layout.addWidget(lbl1)

        return header_layout

    def test_case_list(self):
        list_layout = QVBoxLayout()

        #Simulate Test Cases for UI testing
        item_list = QListWidget()
        for i in range(1, 5):
            item_list.addItem('Test Case' + str(i))
        list_layout.addWidget(item_list)

        return list_layout

    def create_test_case_setting_component(self):
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")
    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    sys.exit(app.exec_())
