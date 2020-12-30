Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "%HOMEDRIVE%%HOMEPATH%\chk_his\chk_his.bat" & Chr(34), 0
Set WinScriptHost = Nothing
