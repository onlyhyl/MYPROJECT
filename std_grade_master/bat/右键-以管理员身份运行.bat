@echo off
set Main_PATH=D:\hyl
set Python_PATH=%Main_PATH%\python-3.7.4-amd64.exe

:: 安装python
echo=
echo           ---------------------------------------------------------------------
echo                             正在安装【学生成绩分析工具】
echo                   本工具无毒无害可食用，可沏上一壶茶，静坐等候。。。
echo=
echo              *** 若中途弹出“禁止”“允许”的相关操作，请选择“允许” ***    
echo           ---------------------------------------------------------------------
start /wait %Python_PATH% /S

:: 设置要永久加入到path环境变量中的路径
for /f "delims=" %%a in ('dir /s /b /ad "C:\*python37"') do (
  set "My_PATH=%%a"
  set "My_PATH2=%%a\Scripts"
)
echo %PATH%>>path_backup.txt
set PATH=%My_PATH%; %PATH%
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%" /f
set PATH=%My_PATH2%; %PATH%
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%" /f

:: 安装pyqt5
pip install PyQt5 PyQt5-tools -i https://pypi.doubanio.com/simple

:: 设置快捷方式
::设置程序或文件的完整路径（必选）
set Program=%Main_PATH%\dist
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
dir /s /b python.exe
timeout /T 10 /NOBREAK
makelnk.vbs
del /f /q makelnk.vbs
exit
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
goto :eof