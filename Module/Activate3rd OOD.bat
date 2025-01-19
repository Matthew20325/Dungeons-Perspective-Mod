@echo off
:: Focus on the Dungeons-Win64-Shipping.exe window
nircmd win activate stitle "Minecraft Dungeons"


:: Wait for a moment to ensure the window is focused




:: Simulate pressing the Enter key
nircmd wait 1000  ; Pause before the next command
nircmd sendkeypress 0xC0
nircmd sendkeypress "c"
nircmd sendkeypress "a"
nircmd sendkeypress "m"
nircmd sendkeypress "e"
nircmd sendkeypress "r"
nircmd sendkeypress "a"
nircmd sendkeypress "spc"
nircmd sendkeypress "t"
nircmd sendkeypress "h"
nircmd sendkeypress "i"
nircmd sendkeypress "r"
nircmd sendkeypress "d"
nircmd sendkeypress "p"
nircmd sendkeypress "e"
nircmd sendkeypress "r"
nircmd sendkeypress "s"
nircmd sendkeypress "o"
nircmd sendkeypress "n"
nircmd sendkeypress "enter"

nircmd sendkeypress 0xC0  ; Simulate pressing F12


nircmd sendkeypress "c"
nircmd sendkeypress "h"
nircmd sendkeypress "a"
nircmd sendkeypress "n"
nircmd sendkeypress "g"
nircmd sendkeypress "e"
nircmd sendkeypress "s"
nircmd sendkeypress "i"
nircmd sendkeypress "z"
nircmd sendkeypress "e"
nircmd sendkeypress "spc"
nircmd sendkeypress "1"
nircmd sendkeypress "enter"

nircmd sendkeypress 0xC0  ; Simulate pressing F12


nircmd sendkeypress "f"
nircmd sendkeypress "o"
nircmd sendkeypress "v"
nircmd sendkeypress "spc"
nircmd sendkeypress "1"
nircmd sendkeypress "2"
nircmd sendkeypress "0"
nircmd sendkeypress "enter"