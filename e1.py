#Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
#run e0 before e1 .... each in a seperate shell
# prep 1) <somepath>\x86\SourceDir\Windows\Microsoft.NET\Framework\v4.0.30319\regtlibv12.exe COMIPC.dll /tlb:COMIPC.tlb /codebase
# prep 2) C:\Windows\System32\regsvr32.exe COMIPC.dll
from comtypes.client import CreateObject
obj = CreateObject("COMIPC")
hEvent = obj.EventCreate
hWait = obj.EventWait
hFileMap = obj.FileMapCreate
Infinite = -1

obj.EventCreate('TestEvent', 1, 0)

rc = obj.EVENTSET("TestEvent")
