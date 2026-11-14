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
# Date: 11:20 2026-11-12

from PythonQt.QtCore import *
from PythonQt.QtGui import *

from PipeCAD.Geometry import *
from PipeCAD.Database import *
from PipeCAD.GUI import MainWindow

class SiteDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Site"))

        self.verticalLayout = QVBoxLayout(self)

        # Name
        self.horizontalLayout = QHBoxLayout()

        self.labelName = QLabel(self.tr("Name"))
        self.textName = QLineEdit()
        self.textName.setMinimumWidth(180)

        self.horizontalLayout.addWidget(self.labelName)
        self.horizontalLayout.addWidget(self.textName)

        self.verticalLayout.addLayout(self.horizontalLayout)

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

        self.textDescription.text = ''
        self.textFunction.text = ''
        self.textPurpose.text = ''
    # reset

    def accept(self):
        name = self.textName.text
        
        try:
            Project.Current.OpenTransaction()

            site = DbElement.Current.Create(0, 'SITE')
            site.Name = name
            site.Description = self.textDescription.text
            site.Function = self.textFunction.text
            site.Purpose = self.textPurpose.text

            Project.Current.CommitTransaction()
        except Exception as ex:
            QMessageBox.critical(self,  '', ex)
            Project.Current.AbortTransaction()
        # try
        
        QDialog.accept(self)
    # accept

# SiteDialog

siteDialog = SiteDialog(MainWindow)

def Create():
    siteDialog.reset()
    siteDialog.show()
# Create
