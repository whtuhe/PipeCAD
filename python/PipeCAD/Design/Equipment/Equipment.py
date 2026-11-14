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
# Date: 11:20 2026-11-02

from PythonQt.QtCore import *
from PythonQt.QtGui import *

from PipeCAD.Geometry import *
from PipeCAD.Database import *
from PipeCAD.GUI import MainWindow

class EquipmentDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Equipment"))

        self.verticalLayout = QVBoxLayout(self)

        # Name
        self.horizontalLayout = QHBoxLayout()

        self.labelName = QLabel(self.tr("Name"))
        self.textName = QLineEdit()
        self.textName.setMinimumWidth(180)

        self.horizontalLayout.addWidget(self.labelName)
        self.horizontalLayout.addWidget(self.textName)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Position
        self.groupBox = QGroupBox(self.tr("Position"))
        self.formLayout = QFormLayout(self.groupBox)

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

        self.verticalLayout.addWidget(self.groupBox)

        # Attributes
        self.groupBox = QGroupBox(self.tr("Attributes"))

        self.formLayout = QFormLayout(self.groupBox)

        self.labelDescription = QLabel(self.tr("Description"))
        self.textDescription = QLineEdit("")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDescription)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textDescription)

        self.labelFunction = QLabel(self.tr("Function"))
        self.textFunction = QLineEdit("")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelFunction)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textFunction)

        self.labelPurpose = QLabel(self.tr("Purpose"))
        self.textPurpose = QLineEdit("")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelPurpose)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textPurpose)

        self.verticalLayout.addWidget(self.groupBox)

        # Action buttons.
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    # setupUi

    def reset(self):
        self.textName.text = ''
        self.textPx.text = '0'
        self.textPy.text = '0'
        self.textPz.text = '0'

        self.textDescription.text = ''
        self.textFunction.text = ''
        self.textPurpose.text = ''
    # reset

    def accept(self):
        name = self.textName.text
        px = float(self.textPx.text)
        py = float(self.textPy.text)
        pz = float(self.textPz.text)
        
        Project.Current.OpenTransaction()

        equipment = DbElement.Current.Create(0, 'EQUI')
        equipment.Name = name
        equipment.Position = Position(px, py, pz)
        equipment.Description = self.textDescription.text
        equipment.Function = self.textFunction.text
        equipment.Purpose = self.textPurpose.text

        Project.Current.CommitTransaction()
        
        QDialog.accept(self)
    # accept

# EquipmentDialog

equipmentDialog = EquipmentDialog(MainWindow)

def CreateEquipment():
    equipmentDialog.reset()
    equipmentDialog.show()
# CreateEquipment

class SubEquipmentDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Sub-Equipment"))

        self.verticalLayout = QVBoxLayout(self)

        # Name
        self.horizontalLayout = QHBoxLayout()

        self.labelName = QLabel(self.tr("Name"))
        self.textName = QLineEdit()
        self.textName.setMinimumWidth(180)

        self.horizontalLayout.addWidget(self.labelName)
        self.horizontalLayout.addWidget(self.textName)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Position
        self.groupBox = QGroupBox(self.tr("Position"))
        self.formLayout = QFormLayout(self.groupBox)

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

        self.verticalLayout.addWidget(self.groupBox)

        # Attributes
        self.groupBox = QGroupBox(self.tr("Attributes"))

        self.formLayout = QFormLayout(self.groupBox)

        self.labelDescription = QLabel(self.tr("Description"))
        self.textDescription = QLineEdit("")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDescription)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textDescription)

        self.labelFunction = QLabel(self.tr("Function"))
        self.textFunction = QLineEdit("")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelFunction)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textFunction)

        self.labelPurpose = QLabel(self.tr("Purpose"))
        self.textPurpose = QLineEdit("")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelPurpose)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textPurpose)

        self.verticalLayout.addWidget(self.groupBox)

        # Action buttons.
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    # setupUi

    def reset(self):
        self.textName.text = ''
        self.textPx.text = '0'
        self.textPy.text = '0'
        self.textPz.text = '0'

        self.textDescription.text = ''
        self.textFunction.text = ''
        self.textPurpose.text = ''
    # reset

    def accept(self):
        name = self.textName.text
        px = float(self.textPx.text)
        py = float(self.textPy.text)
        pz = float(self.textPz.text)
        
        Project.Current.OpenTransaction()

        equipment = DbElement.Current.Create(0, 'EQUI')
        equipment.Name = name
        equipment.Position = Position(px, py, pz)
        equipment.Description = self.textDescription.text
        equipment.Function = self.textFunction.text
        equipment.Purpose = self.textPurpose.text

        Project.Current.CommitTransaction()
        
        QDialog.accept(self)
    # accept

# SubEquipmentDialog

subEquipmentDialog = SubEquipmentDialog(MainWindow)

def CreateSubEquipment():
    subEquipmentDialog.reset()
    subEquipmentDialog.show()
# CreateSubEquipment
