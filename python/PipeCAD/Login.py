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
# Date: 21:16 2026-11-27

from PythonQt.QtCore import *
from PythonQt.QtGui import *
from PythonQt.QtSvg import *

from PipeCAD.Geometry import *
from PipeCAD.Database import *
from PipeCAD.GUI import *


class ProjectDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Project"))
        self.setMinimumWidth(360)

        self.verticalLayout = QVBoxLayout(self)

        # Project Details.
        self.groupProject = QGroupBox(self.tr('Project Details'))

        self.formLayout = QFormLayout(self.groupProject)

        self.textCode = QLineEdit()
        self.textName = QLineEdit()
        self.textDesc = QLineEdit()

        codeRegex = QRegularExpression('^[A-Z]*$')
        nameRegex = QRegularExpression('^[a-zA-Z]*$')

        codeValidator = QRegularExpressionValidator(codeRegex, self.textCode)
        nameValidator = QRegularExpressionValidator(nameRegex, self.textName)

        self.textCode.setValidator(codeValidator)
        self.textName.setValidator(nameValidator)

        self.formLayout.addRow(self.tr('Code'), self.textCode)
        self.formLayout.addRow(self.tr('Name'), self.textName)
        self.formLayout.addRow(self.tr('Description'), self.textDesc)

        self.verticalLayout.addWidget(self.groupProject)

        # Action buttons.
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    # setupUi

    def accept(self):
        code = self.textCode.text.strip()
        name = self.textName.text.strip()

        if not code or not name:
            QMessageBox.critical(self, '', self.tr('Code and Name cannot be empty!'))
            return
        # if

        project = Project.Current
        project.Code = code
        project.Name = name
        project.Description = self.textDesc.text.strip()

        if project.Create(name):
            QMessageBox.information(self, '', self.tr('Create project succeed!'));
            QDialog.accept(self)
        # if

    # accept
# ProjectDialog

class LoginDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("PipeCAD Login"))

        self.verticalLayout = QVBoxLayout(self)

        # Get application path.
        iconsPath = QCoreApplication.applicationDirPath() + '/icons'

        # Project List.
        self.groupProjects = QGroupBox(self.tr('Projects'), self)
        self.groupProjects.setMinimumHeight(180)

        self.horizontalLayout = QHBoxLayout(self.groupProjects)
        self.tableProjects = QTableWidget(self.groupProjects)
        self.tableProjects.setColumnCount(3)
        self.tableProjects.setHorizontalHeaderLabels([self.tr('Code'), self.tr('Name'), self.tr('Description')])
        self.tableProjects.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableProjects.setAlternatingRowColors(True)
        self.tableProjects.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProjects.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableProjects.setGridStyle(Qt.SolidLine)
        self.tableProjects.horizontalHeader().setStretchLastSection(True)
        self.tableProjects.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableProjects.verticalHeader().setMinimumSectionSize(16)
        self.tableProjects.verticalHeader().setDefaultSectionSize(18)
        self.tableProjects.verticalHeader().hide()

        self.horizontalLayout.addWidget(self.tableProjects)

        self.verticalLayout.addWidget(self.groupProjects)

        # Module.
        self.horizontalLayout = QHBoxLayout()

        self.buttonCatalogue = QPushButton()
        self.buttonDesign = QPushButton()
        self.buttonAdmin = QPushButton()

        self.buttonCatalogue.clicked.connect(self.loginCatalogue)
        self.buttonDesign.clicked.connect(self.loginDesign)
        self.buttonAdmin.clicked.connect(self.createProject)

        self.buttonCatalogue.setFixedSize(128, 128)
        self.buttonDesign.setFixedSize(128, 128)
        self.buttonAdmin.setFixedSize(128, 128)

        self.buttonCatalogue.setIcon(QIcon(iconsPath + '/catalog.svg'))
        self.buttonCatalogue.setIconSize(QSize(100, 100))
        self.buttonCatalogue.setToolTip(self.tr('Login Catalogue Module'))

        self.buttonDesign.setIcon(QIcon(iconsPath + '/design.svg'))
        self.buttonDesign.setIconSize(QSize(100, 100))
        self.buttonDesign.setToolTip(self.tr('Login Design Module'))

        self.buttonAdmin.setIcon(QIcon(iconsPath + '/admin.svg'))
        self.buttonAdmin.setIconSize(QSize(100, 100))
        self.buttonAdmin.setToolTip(self.tr('Create Project'))

        self.horizontalLayout.addWidget(self.buttonDesign)
        self.horizontalLayout.addWidget(self.buttonCatalogue)
        self.horizontalLayout.addWidget(self.buttonAdmin)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Version.
        self.horizontalLayout = QHBoxLayout()
        self.labelVersion = QLabel('v.' + Application.GetVersion())
        self.labelVersion.setAlignment(Qt.AlignRight)
        self.horizontalLayout.addWidget(self.labelVersion)
        
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Init projects.
        self.initProjects()
    # setupUi
    
    def initProjects(self):
        projects = Project.GetProjectList()
        size = len(projects)
        self.tableProjects.setRowCount(size)
        for i in range(size):
            project = projects[i]
            self.tableProjects.setItem(i, 0, QTableWidgetItem(project.Code))
            self.tableProjects.setItem(i, 1, QTableWidgetItem(project.Name))
            self.tableProjects.setItem(i, 2, QTableWidgetItem(project.Description))
            self.tableProjects.item(i, 0).setData(Qt.UserRole, project.FileName)
        # for
    # initProjects

    def loginCatalogue(self):
        row = self.tableProjects.currentRow()
        if row < 0:
            QMessageBox.warning(self, '', self.tr('Please select project to login!'))
            return
        # if

        fileName = self.tableProjects.item(row, 0).data(Qt.UserRole)

        Application.Start(fileName, 1)
        QDialog.accept(self)
    # accept

    def loginDesign(self):
        row = self.tableProjects.currentRow()
        if row < 0:
            QMessageBox.warning(self, '', self.tr('Please select project to login!'))
            return
        # if

        fileName = self.tableProjects.item(row, 0).data(Qt.UserRole)

        Application.Start(fileName, 2)
        QDialog.accept(self)
    # accept

    def createProject(self):
        QDialog.accept(self)

        projectDlg = ProjectDialog(self)
        projectDlg.exec()
    # accept

# LoginDialog
