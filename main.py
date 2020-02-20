import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QListWidget, QListWidgetItem, QWidget, QGroupBox,
                             QPushButton, QComboBox, QLineEdit, QSpacerItem)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QGridLayout()

        # Create the Test Case List Component as a GroupBox to add to GridLayout
        upper_layout_test_case_list_component = self.create_test_case_component()
        upper_layout_output_device_component = self.create_device_setting_component()


        # Add the Test Case List and Test Case Settings Component to the main_layout
        main_layout.addWidget(upper_layout_test_case_list_component, 0, 0)
        main_layout.addWidget(upper_layout_output_device_component, 0, 1)

        self.setLayout(main_layout)
        self.show()

    def create_test_case_component(self):
        test_case_component_group_box = QGroupBox()
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

        # Add the main layout for the groupbox with the other layouts already added
        test_case_component_group_box.setLayout(test_case_component_layout)

        return test_case_component_group_box

    # This function creates the necessary buttons for the test case window
    #
    # Return: QHBoxLayout() with the Buttons added
    def test_case_btns(self):
        btn_layout = QHBoxLayout()

        # Create the buttons
        new_btn = QPushButton('Run')
        load_btn = QPushButton('New')
        edit_btn = QPushButton('Edit')
        del_btn = QPushButton('Delete')
        # Add the buttons to the layout
        btn_layout.addWidget(new_btn)
        btn_layout.addWidget(load_btn)
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(del_btn)

        return btn_layout

    # This function creates the header for the test case list
    #
    # Return: QHBoxLayout() containing the test case header
    def test_case_header(self):
        header_layout = QHBoxLayout()

        #Create the label for the Test Cases list
        lbl1 = QLabel('Test Cases')
        header_layout.addWidget(lbl1)

        return header_layout

    # This function creates the list that displays the test cases
    #
    # Return: QVBoxLayout() containing the test case header
    def test_case_list(self):
        list_layout = QVBoxLayout()

        #Simulate Test Cases for UI testing
        item_list = QListWidget()
        for i in range(1, 5):
            item_list.addItem('Test Case' + str(i))
        list_layout.addWidget(item_list)

        return list_layout

    def create_device_setting_component(self):
        device_component_group_box = QGroupBox()
        device_component_layout = QVBoxLayout()
        fast_component = self.create_fast_device_setting_component()
        slow_component = self.create_slow_device_setting_component()
        device_component_layout.addLayout(fast_component)
        device_component_layout.addLayout(slow_component)
        device_component_group_box.setLayout(device_component_layout)
        return device_component_group_box


    def create_fast_device_setting_component(self):
        fast_device_setting_component_assembled = QVBoxLayout()
        fast_device_setting_inner_v = QVBoxLayout()

        # Create the Fast device label with a dropdown containing the valid values
        fast_device_list_layout = QHBoxLayout()
        fast_label = QLabel('Fast Device')
        fast_device_list = QComboBox()
        fast_device_list.setObjectName('fastDevice')
        fast_device_list.addItem("Keithley 2450")
        fast_device_list.addItem("DAQs 9213")
        fast_device_list_layout.addWidget(fast_label)
        fast_device_list_layout.addWidget(fast_device_list)

        # Create the output type dropdown along with the valid options
        fast_device_output_type_layout = QHBoxLayout()
        output_type = QLabel('Output Type')
        fast_device_output_type = QComboBox()
        fast_device_output_type.setObjectName('fastOutputType')
        fast_device_output_type.addItem("Current")
        fast_device_output_type.addItem("Voltage")
        fast_device_output_type_layout.addWidget(output_type)
        fast_device_output_type_layout.addWidget(fast_device_output_type)

        # Create a horizontal layout for the min and max values to be entered so they are inline with their labels
        min_max_layout = QHBoxLayout()
        min_label = QLabel('Min:')
        min_value = QLineEdit()
        min_value.setObjectName('fastMin')
        max_label = QLabel('Max:')
        max_value = QLineEdit()
        max_value.setObjectName('fastMax')
        min_max_layout.addWidget(min_label)
        min_max_layout.addWidget(min_value)
        min_max_layout.addWidget(max_label)
        min_max_layout.addWidget(max_value)

        # Add the source and output type to the inner vertical layout
        fast_device_setting_inner_v.addLayout(fast_device_list_layout)
        fast_device_setting_inner_v.addLayout(fast_device_output_type_layout)

        # Create the Increment amount and timer layouts
        increment_timer_layout = QHBoxLayout()
        increment_amount_layout = QHBoxLayout()
        increment_amount_timer_layout = QVBoxLayout()

        # Create the label, line edit, and layout for the increment amount
        increment_amount_label = QLabel('Increment amount:')
        increment_amount_line_edit = QLineEdit()
        increment_amount_line_edit.setObjectName('fastIncrementAmount')
        increment_amount_layout.addWidget(increment_amount_label)
        increment_amount_layout.addWidget(increment_amount_line_edit)

        # Create the label, line edit, and layout for increment timer
        increment_timer_label = QLabel('Increment timer:')
        increment_timer_line_edit = QLineEdit()
        increment_timer_line_edit.setObjectName('fastIncrementTimer')
        increment_timer_layout.addWidget(increment_timer_label)
        increment_timer_layout.addWidget(increment_timer_line_edit)

        # Add the increment amount and timer layouts to the parent layout
        increment_amount_timer_layout.addLayout(increment_amount_layout)
        increment_amount_timer_layout.addLayout(increment_timer_layout)

        # Add the inner vertical layout and the min_max layout to the main layout
        fast_device_setting_component_assembled.addLayout(fast_device_setting_inner_v)
        fast_device_setting_component_assembled.addLayout(min_max_layout)
        fast_device_setting_component_assembled.addLayout(increment_amount_timer_layout)

        return fast_device_setting_component_assembled

    def create_slow_device_setting_component(self):
        slow_device_setting_component_assembled = QVBoxLayout()
        slow_device_setting_inner_v = QVBoxLayout()

        # Create the Slow device label with a drop down containing the valid values
        slow_device_list_layout = QHBoxLayout()
        slow_label = QLabel('Slow Device')
        slow_device_list = QComboBox()
        slow_device_list.setObjectName('slowDevice')
        slow_device_list.addItem("Keithley 2450")
        slow_device_list.addItem("DAQs 9213")
        slow_device_list_layout.addWidget(slow_label)
        slow_device_list_layout.addWidget(slow_device_list)

        # Create the output type dropdown along with the valid options
        slow_output_type_layout = QHBoxLayout()
        output_type_label = QLabel('Output Type')
        slow_device_output_type = QComboBox()
        slow_device_output_type.setObjectName('slowOutputType')
        slow_device_output_type.addItem("Current")
        slow_device_output_type.addItem("Voltage")
        slow_output_type_layout.addWidget(output_type_label)
        slow_output_type_layout.addWidget(slow_device_output_type)

        # Create a horizontal layout for the min and max values to be entered so they are inline with their labels
        min_max_layout = QHBoxLayout()
        min_label = QLabel('Min:')
        min_value = QLineEdit()
        min_value.setObjectName('slowMin')
        max_label = QLabel('Max:')
        max_value = QLineEdit()
        max_value.setObjectName('slowMax')
        min_max_layout.addWidget(min_label)
        min_max_layout.addWidget(min_value)
        min_max_layout.addWidget(max_label)
        min_max_layout.addWidget(max_value)

        # Add the source and output type to the inner vertical layout
        slow_device_setting_inner_v.addLayout(slow_device_list_layout)
        slow_device_setting_inner_v.addLayout(slow_output_type_layout)

        # Create the Increment amount and timer layouts
        increment_timer_layout = QHBoxLayout()
        increment_amount_layout = QHBoxLayout()
        increment_amount_timer_layout = QVBoxLayout()

        # Create the label, line edit, and layout for the increment amount
        increment_amount_label = QLabel('Increment amount:')
        increment_amount_line_edit = QLineEdit()
        increment_amount_line_edit.setObjectName('slowIncrementAmount')
        increment_amount_layout.addWidget(increment_amount_label)
        increment_amount_layout.addWidget(increment_amount_line_edit)

        # Create the label, line edit, and layout for increment timer
        increment_timer_label = QLabel('Increment timer:')
        increment_timer_line_edit = QLineEdit()
        increment_timer_line_edit.setObjectName('slowIncrementTimer')
        increment_timer_layout.addWidget(increment_timer_label)
        increment_timer_layout.addWidget(increment_timer_line_edit)

        # Add the increment amount and timer layouts to the parent layout
        increment_amount_timer_layout.addLayout(increment_amount_layout)
        increment_amount_timer_layout.addLayout(increment_timer_layout)

        # Add the inner vertical layout and the min_max layout to the main layout
        slow_device_setting_component_assembled.addLayout(slow_device_setting_inner_v)
        slow_device_setting_component_assembled.addLayout(min_max_layout)
        slow_device_setting_component_assembled.addLayout(increment_amount_timer_layout)

        return slow_device_setting_component_assembled


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.setWindowTitle("Francois Amet's Research on Resistance and Electromagnetism")
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
