
@echo off

set PATH=%PATH%;D:\Code\3rdparty\Python\Python314\Scripts;

rem Update translation for python file.
pyside6-lupdate -extensions py python -ts translations/zh_CN.ts

pause
