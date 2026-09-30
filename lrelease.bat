
@echo off

set PATH=%PATH%;D:\Code\3rdparty\Python\Python314\Scripts;

rem Release translations file to qm file.
pyside6-lrelease translations/zh_CN.ts -qm i18n/zh_CN.qm

pause
