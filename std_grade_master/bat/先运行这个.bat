@echo off
echo=
echo           ---------------------------------------------------------------------
echo                             ���ڰ�װ��ѧ���ɼ��������ߡ�
echo                   �������޶��޺���ʳ�ã�������һ���裬�����Ⱥ򡣡���
echo=
echo              *** ����;��������������ֹ������ز�������ѡ������ ***    
echo           ---------------------------------------------------------------------
::timeout /T 10 /NOBREAK
start /wait python-3.7.4-amd64.exe /S

::���ó�����ļ�������·������ѡ��
set Program=%cd%\dist
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
timeout /T 10 /NOBREAK
makelnk.vbs
del /f /q makelnk.vbs
exit
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
goto :eof