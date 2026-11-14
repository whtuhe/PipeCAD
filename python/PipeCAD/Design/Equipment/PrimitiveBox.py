# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :: Welcome to PipeCAD!                                      ::
# ::  ____                        ____     ______  ____       ::
# :: /\  _`\   __                /\  _`\  /\  _  \/\  _`\     ::
# :: \ \ \L\ \/\_\  _____      __\ \ \/\_\\ \ \L\ \ \ \/\ \   ::
# ::  \ \ ,__/\/\ \/\ '__`\  /'__`\ \ \/_/_\ \  __ \ \ \ \ \  ::
# ::   \ \ \/  \ \ \ \ \L\ \/\  __/\ \ \L\ \\ \ \/\ \ \ \_\ \ ::
# ::    \ \_\   \ \_\ \ ,__/\ \____\\ \____/ \ \_\ \_\ \____/ ::
# ::     \/_/    \/_/\ \ \/  \/____/ \/___/   \/_/\/_/\/___/  ::
# ::                  \ \_\                                   ::
# ::                   \/_/                                   ::
# ::                                                          ::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# PipeCAD - Piping Design Software.
# Copyright (C) 2026 Wuhan TUHE Tech Co., Ltd.
# Author: Shing Liu(whtuhe@qq.com)
# Date: 11:20 2026-11-03

from PythonQt.QtCore import *
from PythonQt.QtGui import *

from PipeCAD.Geometry import *
from PipeCAD.Database import *
from PipeCAD.GUI import MainWindow

class BoxDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Box"))

        self.horizontalLayout = QHBoxLayout(self)
        self.verticalLayout = QVBoxLayout()

        self.formLayout = QFormLayout()

        # Name
        self.comboName = QComboBox()
        self.textName = QLineEdit()
        self.textName.setMinimumWidth(150)

        self.comboName.addItem(self.tr("Create"))
        self.comboName.addItem(self.tr("Modify"))
        self.comboName.activated.connect(self.activateName)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.comboName)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textName)

        self.labelNegative = QLabel(self.tr("Negative"))
        self.checkNegative = QCheckBox()

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelNegative)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkNegative)

        self.verticalLayout.addLayout(self.formLayout)

        # Horizontal Line
        self.horizontalLine = QFrame()
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)
        self.verticalLayout.addWidget(self.horizontalLine)

        # Dimensions.
        self.formLayout = QFormLayout()

        self.labelXlen = QLabel(self.tr("X Length"))
        self.textXlen = QLineEdit("0.0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelXlen)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textXlen)
        
        self.labelYlen = QLabel(self.tr("Y Length"))
        self.textYlen = QLineEdit("0.0")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelYlen)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textYlen)
        
        self.labelZlen = QLabel(self.tr("Z Length"))
        self.textZlen = QLineEdit("0.0")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelZlen)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textZlen)

        self.verticalLayout.addLayout(self.formLayout)

        # Horizontal Line
        self.horizontalLine = QFrame()
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)
        self.verticalLayout.addWidget(self.horizontalLine)

        # Position.
        self.formLayout = QFormLayout()

        self.labelPx = QLabel(self.tr("East"))
        self.textPx = QLineEdit("0.0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelPx)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textPx)

        self.labelPy = QLabel(self.tr("North"))
        self.textPy = QLineEdit("0.0")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelPy)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textPy)

        self.labelPz = QLabel(self.tr("Up"))
        self.textPz = QLineEdit("0.0")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelPz)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textPz)

        self.verticalLayout.addLayout(self.formLayout)

        # Vertical Spacer.
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

        # Action buttons.
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.verticalLayout.addWidget(self.buttonBox)

        self.horizontalLayout.addLayout(self.verticalLayout)

        # Diagram
        self.labelDiagram = QLabel()
        self.labelDiagram.setMinimumSize(QSize(280, 360))
        self.labelDiagram.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelDiagram.setPixmap(QPixmap(":/icons/diagram_box.svg"))
        self.horizontalLayout.addWidget(self.labelDiagram)
    # setupUi

    def activateName(self):
        index = self.comboName.currentIndex
        if index != 0:
            box = DbElement.Current
            if box.Type != 'BOX':
                QMessageBox.warning(self, '', self.tr('Please select Box to modify!'))
                return
            # if

            pos = box.Position
            self.textPx.text = str(pos.X)
            self.textPy.text = str(pos.Y)
            self.textPz.text = str(pos.Z)

            self.textXlen.text = str(box.Xlength)
            self.textYlen.text = str(box.Ylength)
            self.textZlen.text = str(box.Zlength)
        # if
    # activateName

    def createBox(self):

        try:
            px = float(self.textPx.text)
            py = float(self.textPy.text)
            pz = float(self.textPz.text)

            lx = float(self.textXlen.text)
            ly = float(self.textYlen.text)
            lz = float(self.textZlen.text)

            Project.Current.OpenTransaction()

            box = DbElement.Current.Create(0, 'BOX')
            box.Name = self.textName.text
            box.Position = Position(px, py, pz)
            box.Xlength = lx
            box.Ylength = ly
            box.Zlength = lz

            Project.Current.CommitTransaction()

        except Exception as ex:
            QMessageBox.critical(self, '', ex)
            Project.Current.AbortTransaction()
        # try
    # createBox

    def modifyBox(self):

        try:
            px = float(self.textPx.text)
            py = float(self.textPy.text)
            pz = float(self.textPz.text)

            lx = float(self.textXlen.text)
            ly = float(self.textYlen.text)
            lz = float(self.textZlen.text)

            Project.Current.OpenTransaction()

            box = DbElement.Current
            box.Position = Position(px, py, pz)
            box.Xlength = lx
            box.Ylength = ly
            box.Zlength = lz

            Project.Current.CommitTransaction()

        except Exception as ex:
            QMessageBox.critical(self, '', ex)
            Project.Current.AbortTransaction()
        # try
    # modifyBox

    def accept(self):
        index = self.comboName.currentIndex
        if index == 0:
            self.createBox()
        else:
            self.modifyBox()
        # if

        QDialog.accept(self)
    # accept

# BoxDialog

boxDialog = BoxDialog(MainWindow)

def Create():
    boxDialog.show()
# CreateBox
