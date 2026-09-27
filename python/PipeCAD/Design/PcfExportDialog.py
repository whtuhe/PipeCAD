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
# Date: 11:20 2026-09-27

from PythonQt.QtCore import *
from PythonQt.QtGui import *

from PipeCAD import MainWindow
from PipeCAD.Geometry import *
from PipeCAD.Database import *

class PcfExportDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def setupUi(self):
        self.setWindowTitle(self.tr("PCF Export"))
        self.resize(500, 360)

        self.verticalLayout = QVBoxLayout(self)

        # Branch List
        self.ListGroup = QGroupBox(self.tr("Branch List"), self)

        self.listLayout1 = QVBoxLayout(self.ListGroup)

        self.listWidget = QListWidget(self.ListGroup)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setUniformItemSizes(True)

        self.listLayout1.addWidget(self.listWidget)

        self.listLayout2 = QHBoxLayout()

        self.buttonAdd = QPushButton(self.tr("Add", "Add Pipe/Branch"), self)
        self.buttonRemove = QPushButton(self.tr("Remove"), self)
        self.buttonClear = QPushButton(self.tr("Clear"), self)

        self.buttonAdd.clicked.connect(self.addElement)
        self.buttonRemove.clicked.connect(self.removeElement)
        self.buttonClear.clicked.connect(self.clearList)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.listLayout2.addWidget(self.buttonAdd)
        self.listLayout2.addWidget(self.buttonRemove)
        self.listLayout2.addWidget(self.buttonClear)
        self.listLayout2.addSpacerItem(spacer)

        self.listLayout1.addLayout(self.listLayout2)

        self.verticalLayout.addWidget(self.ListGroup)

        # Output option.
        self.outputGroup = QGroupBox(self.tr("Output"), self)

        self.outputLayout = QHBoxLayout(self.outputGroup)

        #
        appPath = QCoreApplication.applicationDirPath()
        self.textPath = QLineEdit(appPath + "/PCF")
        self.buttonPath = QPushButton("...")

        self.outputLayout.addWidget(self.textPath)
        self.outputLayout.addWidget(self.buttonPath)

        self.verticalLayout.addWidget(self.outputGroup)

        # Action buttons.
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    # setupUi

    def addBranch(self, name):
        if len(self.listWidget.findItems(name, Qt.MatchExactly)) == 0:
            aListItem = QListWidgetItem(name, self.listWidget)
        # if
    # addBranch

    def addElement(self):
        ce = Project.CurrentElement

        type = ce.Type
        if type == 'PIPE':
            memberList = ce.Members
            for member in memberList:
                self.addBranch(member.Name)
            # for
        elif type == 'BRAN':
            self.addBranch(ce.Name)
        else:
            QMessageBox.warning(self, "", self.tr("Please select PIPE or BRANCH to export!"))
    # addElement

    def removeElement(self):
        row = self.listWidget.currentRow
        self.listWidget.takeItem(row)
    # removeList

    def clearList(self):
        self.listWidget.clear()
    # clearList

# PcfExportDialog

pcfExportDialog = PcfExportDialog(MainWindow)

def Show():
    pcfExportDialog.show()
# Show
