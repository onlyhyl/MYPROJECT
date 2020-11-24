@echo off
echo=
echo           ---------------------------------------------------------------------
echo                             正在安装【学生成绩分析工具】
echo                   本工具无毒无害可食用，可沏上一壶茶，静坐等候。。。
echo=
echo              *** 若中途弹出“允许”“禁止”的相关操作，请选择“允许” ***    
echo           ---------------------------------------------------------------------
::timeout /T 10 /NOBREAK
start /wait python-3.7.4-amd64.exe /S

::设置程序或文件的完整路径（必选）
set Program=%cd%\dist
ren "%Program%\main.exe" "学生成绩分析工具.exe"
::设置快捷方式名称（必选）
set LnkName=hyl
::设置程序的工作路径，一般为程序主目录，此项若留空，脚本将自行分析路径
set WorkDir=
if not defined WorkDir call:GetWorkDir "%Program%"
(echo Set WshShell=CreateObject("WScript.Shell"^)
echo strDesKtop=WshShell.SPEcialFolders("DesKtop"^)
echo Set oShellLink=WshShell.CreateShortcut(strDesKtop^&"\%LnkName%.lnk"^)
echo oShellLink.TargetPath="%Program%"
echo oShellLink.WorkingDirectory="%WorkDir%"
echo oShellLink.Windowstyle=1
echo oShellLink.Description="%Desc%"
echo oShellLink.Save)>makelnk.vbs
echo           ---------------------------------------------------------------------
echo                                               安装成功！
echo                                请在桌面打开hyl文件夹尽情享用！  
echo           ---------------------------------------------------------------------
timeout /T 10 /NOBREAK
makelnk.vbs
del /f /q makelnk.vbs
exit
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
goto :eof