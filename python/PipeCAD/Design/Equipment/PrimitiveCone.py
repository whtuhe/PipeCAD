# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :: Welcome to PipeCAD!                                      ::
# ::  ____                        ____     ______  ____       ::
# :: /\  _`\   __                /\  _`\  /\  _  \/\  _`\     ::
# :: \ \ \L\ \/\_\  _____      __\ \ \/\_\\ \ \L\ \ \ \/\ \   ::
# ::  \ \ ,__/\/\ \/\ '__`\  /'__`\ \ \/_/_\ \  __ \ \ \ \ \  ::
# ::   \ \ \/  \ \ \ \ \L\ \/\  __/\ \ \L\ \\ \/\ \ \ \_\ \ ::
# ::    \ \_\   \ \_\ \ ,__/\ \____\\ \____/ \ \_\ \_\ \____/ ::
# ::     \/_/    \/_/\ \ \/  \/____/ \/___/   \/_/\/_/\/___/  ::
# ::                  \ \_\                                   ::
# ::                   \/_/                                   ::
# ::                                                          ::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# PipeCAD - Piping Design Software.
# Copyright (C) 2026 Wuhan TUHE Tech Co., Ltd.
#
# 设备基本体：圆锥体 Cone 的创建与修改。
# 界面风格与 PrimitiveBox.py / PrimitiveCylinder.py 保持一致。
#
# 圆锥体尺寸参数：
#   Dtop    顶部直径（0 表示尖顶圆锥）
#   Dbottom 底部直径
#   Height  高度
#
# 建模约定：Position 位于锥体中心（Height / 2 处），沿 Z 方向拉伸。

from PythonQt.QtCore import *
from PythonQt.QtGui import *

from PipeCAD.Geometry import *
from PipeCAD.Database import *
from PipeCAD.GUI import MainWindow

class ConeDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Create Cone"))

        self.horizontalLayout = QHBoxLayout(self)
        self.verticalLayout = QVBoxLayout()

        # Name / Create-Modify selector.
        self.formLayout = QFormLayout()

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

        self.labelDtop = QLabel(self.tr("Dtop"))
        self.textDtop = QLineEdit("0.0")
        self.textDtop.setToolTip(self.tr("Top Diameter"))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDtop)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textDtop)

        self.labelDbottom = QLabel(self.tr("Dbottom"))
        self.textDbottom = QLineEdit("100.0")
        self.textDbottom.setToolTip(self.tr("Bottom Diameter"))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDbottom)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textDbottom)

        self.labelHeight = QLabel(self.tr("Height"))
        self.textHeight = QLineEdit("100.0")
        self.textHeight.setToolTip(self.tr("Height"))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelHeight)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.textHeight)

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
        self.labelDiagram.setPixmap(QPixmap(":/icons/diagram_cone.svg"))
        self.horizontalLayout.addWidget(self.labelDiagram)
    # setupUi

    def activateName(self):
        index = self.comboName.currentIndex
        if index != 0:
            cone = DbElement.Current
            if cone.Type != 'CONE':
                QMessageBox.warning(self, '', self.tr('Please select Cone to modify!'))
                self.comboName.setCurrentIndex(0)
                return
            # if

            pos = cone.Position
            self.textPx.text = str(pos.X)
            self.textPy.text = str(pos.Y)
            self.textPz.text = str(pos.Z)

            self.textName.text = cone.Name
            self.textDtop.text = str(cone.Dtop)
            self.textDbottom.text = str(cone.Dbottom)
            self.textHeight.text = str(cone.Height)
        # if
    # activateName

    def createCone(self):
        try:
            px = float(self.textPx.text)
            py = float(self.textPy.text)
            pz = float(self.textPz.text)

            dtop = float(self.textDtop.text)
            dbottom = float(self.textDbottom.text)
            height = float(self.textHeight.text)

            if dtop < 0.0 or dbottom < 0.0 or height <= 0.0:
                raise ValueError(self.tr('Dtop/Dbottom must be >= 0 and Height > 0.'))

            Project.Current.OpenTransaction()

            cone = DbElement.Current.Create(0, 'CONE')
            cone.Name = self.textName.text
            cone.Position = Position(px, py, pz)
            cone.Dtop = dtop
            cone.Dbottom = dbottom
            cone.Height = height

            Project.Current.CommitTransaction()

        except Exception as ex:
            QMessageBox.critical(self, '', str(ex))
            Project.Current.AbortTransaction()
        # try
    # createCone

    def modifyCone(self):
        try:
            px = float(self.textPx.text)
            py = float(self.textPy.text)
            pz = float(self.textPz.text)

            dtop = float(self.textDtop.text)
            dbottom = float(self.textDbottom.text)
            height = float(self.textHeight.text)

            if dtop < 0.0 or dbottom < 0.0 or height <= 0.0:
                raise ValueError(self.tr('Dtop/Dbottom must be >= 0 and Height > 0.'))

            Project.Current.OpenTransaction()

            cone = DbElement.Current
            cone.Position = Position(px, py, pz)
            cone.Dtop = dtop
            cone.Dbottom = dbottom
            cone.Height = height

            Project.Current.CommitTransaction()

        except Exception as ex:
            QMessageBox.critical(self, '', str(ex))
            Project.Current.AbortTransaction()
        # try
    # modifyCone

    def accept(self):
        index = self.comboName.currentIndex
        if index == 0:
            self.createCone()
        else:
            self.modifyCone()
        # if

        QDialog.accept(self)
    # accept

# ConeDialog

coneDialog = ConeDialog(MainWindow)

def Create():
    coneDialog.comboName.setCurrentIndex(0)
    coneDialog.show()
# Create
