---
name: pipecad-dev-python
description: PipeCAD Python 二次开发专家技能。当用户需要编写、调试、解释或审查PipeCAD Python代码--数据访问、元素创建/删除/遍历、属性读写、几何与位置计算、数据库事件处理时，务必使用本技能。
metadata:
  suite: pipecad-dev-skills
  version: "0.1.0"
---

# PipeCAD Python 开发指南

帮助用户使用 PipeCAD 的 Python 接口进行二次开发：查找 API、编写代码、解释现有代码。

## 使用流程

**确定命名空间**：先判断任务属于哪个领域，对应命名空间如下：

   | 领域 | 命名空间 | 关键类型 |
   |------|----------|----------|
   | 独立应用入口 | `PipeCAD.Standalone` | `Standalone` |
   | 项目/数据库 | `PipeCAD.Database` | `Project`, `DbElement`, `DbAttribute`, `DbElementType`,  |
   | 几何（点/线/面/方向） | `PipeCAD.Geometry` | `Position`, `Orientation`, `Direction`, `Line`, `Plane`, `LimitsBox`, `Axis` |
   | 图形接口 | `PipeCAD.Graphics` | `DrawListManager`, `DrawList`, `Colour`, `Aid` |

## 核心概念

务必理解 PipeCAD 中的核心概念：

- **`DbElement`**：数据库元素的句柄，操作所有的数据对象。判断"空"元素必须用 `IsNull` 属性（`element.IsNull`），不能与 null 比较。使用之前最好使用属性先判断是否有效 `IsValid`。

- **`DbAttribute`**：属性标识，为了简化属性的查询，统一使用字符串。如 `Name`, `Type`, `Owner`, `Position`等。

- **`DbElementType`**：元素类型标识，为了简化类型的查询，统一使用字符串。如 `SITE`, `ZONE`, `PIPE`等。

- **属性值**：用 `DbElement.GetAsString/GetBool/GetDouble/GetInteger` 等直接取；写值用 `SetAttribute(DbAttribute, 值)`，重载覆盖 string/int/double/bool/DbElement/DbElement[]/Position/Orientation/Direction 等。

所有属性的名称，类型及描述请查看 `data/Attribute.md` 。所有元素类型、包含的属性及层级关系请查看 `data/ElementType.md`。

## 任务模式

### 1. GUI开发

用户界面开发主要使用 `PythonQt`，语法与 `PySide` 和 `PyQt` 类似， 即 `Qt` 中界面相关的类和功能都可以使用。需要引入 `PythonQt` 相应的库：

```py
from PythonQt.QtCore import *
from PythonQt.QtGui import *
```

下面代码示例为一个简单的窗口实现：

```py
from PythonQt.QtCore import *
from PythonQt.QtGui import *

class HelloDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi()
    # __init__

    def tr(self, text, comment = None):
        return QCoreApplication.translate(self.__class__.__name__, text, comment)
    # tr

    def setupUi(self):
        self.setWindowTitle(self.tr("Hello PipeCAD"))

        self.verticalLayout = QVBoxLayout(self)

        self.labelHello = QLabel(self.tr("Hello PipeCAD!"))

        self.verticalLayout.addWidget(self.labelHello)

        # Action buttons.
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    # setupUi

# HelloDialog
```

对于用户界面上需要被翻译的字符串，必须实现 `tr()` 函数，需要翻译的字符必须使用英文，并调用 `self.tr()`。将上述代码保存为 `PipeCAD/python/Design/General/Hello.py`，在 `PipeCAD` 中的命令窗口中输入以下命令即可以显示出界面窗口：

```py
from PipeCAD.Design.General import Hello

dlg = Hello.HelloDialog()
dlg.show()

```

### 2. 项目接口



### 3. 查找元素

### 4. 创建元素

### 5. 删除元素

### 6. 读写属性

### 7. 几何属性

### 8. 事件处理

### 9. 事务机制

### 10. 图形接口


## 参考文档

完整 API 参考（每个类型的全部成员签名与描述）位于本 skill 的：

- `api/<Namespace>/INDEX.md` — 每个命名空间的类型索引（含一句话描述）
- `api/<Namespace>/<完整类型名>.md` — 单个类型文档，包含每个类的名称，功能描述及可用的属性和函数列表。

给出 API 建议后，若用户需要精确签名，务必打开对应类型文档核对，不要凭记忆写。
