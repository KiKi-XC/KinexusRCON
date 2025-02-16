from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ServersListInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ServersListInterface")

        layout = QVBoxLayout(self)
        label = QLabel("Servers List", self)
        label.setObjectName("serversLabel")
        layout.addWidget(label)
        layout.addStretch(1)
