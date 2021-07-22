; Spiffy text, Voidstar Lab
Numpad1::
    Send ^a
    Send ^x
    RunWait, pythonw.exe spiff.py spiff_voidstar.txt
    Send ^v
    Send {Enter}
    Return

; Spiffy text, regional indicators (fallback)
Numpad2::
    Send ^a
    Send ^x
    RunWait, pythonw.exe spiff.py spiff_regional.txt
    Send ^v
    Send {Enter}
    Return
