@echo off
set Main_PATH=D:\hyl
set Python_PATH=%Main_PATH%\python-3.7.4-amd64.exe

:: ��װpython
echo=
echo           ---------------------------------------------------------------------
echo                             ���ڰ�װ��ѧ���ɼ��������ߡ�
echo                   �������޶��޺���ʳ�ã�������һ���裬�����Ⱥ򡣡���
echo=
echo              *** ����;��������ֹ������������ز�������ѡ������ ***    
echo           ---------------------------------------------------------------------
start /wait %Python_PATH% /S

:: ����Ҫ���ü��뵽path���������е�·��
for /f "delims=" %%a in ('dir /s /b /ad "C:\*python37"') do (
  set "My_PATH=%%a"
  set "My_PATH2=%%a\Scripts"
)
echo %PATH%>>path_backup.txt
set PATH=%My_PATH%; %PATH%
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%" /f
set PATH=%My_PATH2%; %PATH%
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%" /f

:: ��װpyqt5
pip install PyQt5 PyQt5-tools -i https://pypi.doubanio.com/simple

:: ���ÿ�ݷ�ʽ
::���ó�����ļ�������·������ѡ��
set Program=%Main_PATH%\dist
ren "%Program%\main.exe" "ѧ���ɼ���������.exe"
::���ÿ�ݷ�ʽ���ƣ���ѡ��
set LnkName=hyl
::���ó���Ĺ���·����һ��Ϊ������Ŀ¼�����������գ��ű������з���·��
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
echo                                               ��װ�ɹ���
echo                                ���������hyl�ļ��о������ã�  
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