import win32evtlog

h = win32evtlog.OpenEventLog(None,"Application")



flags= win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ

print("flags", flags)

records=win32evtlog.ReadEventLog(h, flags, 0)

print("records=",records)
print(records[0].SourceName)
print(records[0].TimeWritten.Format())
print(len(records))


