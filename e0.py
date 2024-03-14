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
rc = obj.EventWait('TestEvent', Infinite)
