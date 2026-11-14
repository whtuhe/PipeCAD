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
# Date: 16:40 2026-11-13

from PythonQt.QtCore import *
from PythonQt.QtGui import *

from PipeCAD.Geometry import *
from PipeCAD.Database import *
from PipeCAD.GUI import MainWindow

class CylinderDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Cylinder"))

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

        self.labelDiameter = QLabel(self.tr("Diameter"))
        self.textDiameter = QLineEdit("0.0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDiameter)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textDiameter)

        self.labelHeight = QLabel(self.tr("Height"))
        self.textHeight = QLineEdit("0.0")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelHeight)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textHeight)

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
        self.labelDiagram.setPixmap(QPixmap(":/icons/diagram_cylinder.svg"))
        self.horizontalLayout.addWidget(self.labelDiagram)
    # setupUi

    def activateName(self):
        index = self.comboName.currentIndex
        if index != 0:
            cylinder = DbElement.Current
            if cylinder.Type != 'CYLI':
                QMessageBox.warning(self, '', self.tr('Please select Cylinder to modify!'))
                return
            # if
            
            pos = cylinder.Position
            self.textPx.text = str(pos.X)
            self.textPy.text = str(pos.Y)
            self.textPz.text = str(pos.Z)
            
            self.textDiameter.text = str(cylinder.Diameter)
            self.textHeight.text = str(cylinder.Height)
        # if
    # activateName

    def createCylinder(self):

        try:
            px = float(self.textPx.text)
            py = float(self.textPy.text)
            pz = float(self.textPz.text)

            d = float(self.textDiameter.text)
            h = float(self.textHeight.text)

            Project.Current.OpenTransaction()

            cylinder = DbElement.Current.Create(0, 'CYLI')
            cylinder.Name = self.textName.text
            cylinder.Position = Position(px, py, pz)
            cylinder.Diameter = d
            cylinder.Height = h

            Project.Current.CommitTransaction()

        except Exception as ex:
            QMessageBox.critical(self, '', ex)
            Project.Current.AbortTransaction()
        # try
    # createCylinder

    def modifyCylinder(self):

        try:
            px = float(self.textPx.text)
            py = float(self.textPy.text)
            pz = float(self.textPz.text)

            d = float(self.textDiameter.text)
            h = float(self.textHeight.text)

            Project.Current.OpenTransaction()

            cylinder = DbElement.Current
            cylinder.Position = Position(px, py, pz)
            cylinder.Diameter = d
            cylinder.Height = h

            Project.Current.CommitTransaction()

        except Exception as ex:
            QMessageBox.critical(self, '', ex)
            Project.Current.AbortTransaction()
        # try
    # modifyCylinder

    def accept(self):
        index = self.comboName.currentIndex
        if index == 0:
            self.createCylinder()
        else:
            self.modifyCylinder()
        # if

        QDialog.accept(self)
    # accept

# CylinderDialog

cylinderDialog = CylinderDialog(MainWindow)

def Create():
    cylinderDialog.show()
# CreateCylinder
