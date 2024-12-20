import ctypes

def CheckTitles():
    # Access user32.dll functions
    user32 = ctypes.windll.user32
    EnumWindows = user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = user32.GetWindowTextW
    GetWindowTextLength = user32.GetWindowTextLengthW
    IsWindowVisible = user32.IsWindowVisible

    # List of forbidden window titles (e.g., common debugger, disassembler, and hacker tools)
    forbidden_titles = {
        "proxifier", "graywolf", "extremedumper", "zed", "exeinfope", "dnspy",
        "titanHide", "ilspy", "titanhide", "x32dbg", "codecracker", "simpleassembly",
        "process hacker 2", "pc-ret", "http debugger", "Centos", "process monitor",
        "debug", "ILSpy", "reverse", "simpleassemblyexplorer", "process", "de4dotmodded",
        "dojandqwklndoqwd-x86", "sharpod", "folderchangesview", "fiddler", "die", "pizza",
        "crack", "strongod", "ida -", "brute", "dump", "StringDecryptor", "wireshark",
        "debugger", "httpdebugger", "gdb", "kdb", "x64_dbg", "windbg", "x64netdumper",
        "petools", "scyllahide", "megadumper", "reversal", "ksdumper v1.1 - by equifox",
        "dbgclr", "HxD", "monitor", "peek", "ollydbg", "ksdumper", "http", "wpe pro", "dbg",
        "httpanalyzer", "httpdebug", "PhantOm", "kgdb", "james", "x32_dbg", "proxy", "phantom",
        "mdbg", "WPE PRO", "system explorer", "de4dot", "X64NetDumper", "protection_id",
        "charles", "systemexplorer", "pepper", "hxd", "procmon64", "MegaDumper", "ghidra", "xd",
        "0harmony", "dojandqwklndoqwd", "hacker", "process hacker", "SAE", "mdb", "checker",
        "harmony", "Protection_ID", "PETools", "scyllaHide", "x96dbg", "systemexplorerservice",
        "folder", "mitmproxy", "dbx", "sniffer", "Process Hacker", "Process Explorer",
        "Sysinternals", "www.sysinternals.com", "binary ninja"
    }

    # Callback function to process each window found
    def foreach_window(hwnd, lParam):
        # Get window title length and content
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        title = buff.value

        # If the window is visible and its title is in the forbidden list, return True (found forbidden title)
        if IsWindowVisible(hwnd) and title.lower() in forbidden_titles:
            return True
        return False

    # Enumerate all windows and check for forbidden titles
    found_forbidden = EnumWindows(EnumWindowsProc(foreach_window), 0)
    
    # Return True if a forbidden title is found, else False
    return found_forbidden


# IMPORTANT NOTICE:
# This function checks the titles of all open windows on the system and compares them with a predefined list of forbidden titles.
# It identifies windows related to tools commonly associated with debugging, reverse engineering, malware analysis, and hacking.
#
# Key points to consider:
# - The list of forbidden titles is comprehensive but may not cover all possible tools.
# - This check only scans the visible window titles, so hidden or minimized tools may not be detected.
# - This method relies on `EnumWindows` to enumerate all open windows and `GetWindowText` to retrieve their titles.
#
# Use this function responsibly:
# - This function should not be used for unauthorized monitoring of users or systems.
# - The presence of certain titles does not necessarily indicate malicious activity; tools may be used for legitimate purposes.
# - Always consider the context and permissions before taking any action based on the results of this function.