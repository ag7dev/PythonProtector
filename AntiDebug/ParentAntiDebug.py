import ctypes
import os
import pathlib
import sys

# Define constants for process querying and the max path size
PROCESS_QUERY_INFORMATION = 0x0400
MAX_PATH = 260 

# Define a structure to hold basic information about a process
class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("Reserved1", ctypes.c_void_p),
        ("PebBaseAddress", ctypes.c_void_p),
        ("Reserved2", ctypes.c_void_p * 2),
        ("UniqueProcessId", ctypes.c_ulong),
        ("InheritedFromUniqueProcessId", ctypes.c_void_p)
    ]

# Load ntdll.dll to use system-level process information functions
ntdll = ctypes.WinDLL("ntdll.dll")
ntquery = ntdll.NtQueryInformationProcess
ntquery.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(PROCESS_BASIC_INFORMATION), ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]

# Function to query process information using NtQueryInformationProcess
def NtQueryProc(handle, class_type):
    proc_basic_info = PROCESS_BASIC_INFORMATION()
    return_length = ctypes.c_uint32()
    
    # Call NtQueryInformationProcess to get basic information about the process
    status = ntquery(handle, class_type, ctypes.byref(proc_basic_info), ctypes.sizeof(proc_basic_info), ctypes.byref(return_length))
    
    # If the query fails, raise an exception
    if status != 0x0:
        raise ctypes.WinError(ctypes.get_last_error())
    
    return proc_basic_info

# Function to get the full image name (executable path) of a process
def QueryImageName(handle):
    name_buffer = ctypes.create_unicode_buffer(MAX_PATH)
    size = ctypes.c_uint32(MAX_PATH)
    
    # Query the full process image name
    if not ctypes.windll.kernel32.QueryFullProcessImageNameW(handle, 0, name_buffer, ctypes.byref(size)):
        raise ctypes.WinError(ctypes.get_last_error())
    
    return name_buffer.value

# Function to get the current process name
def CurrentProcName():
    return pathlib.Path(os.path.abspath(sys.argv[0])).name

# Function to check if the parent process is likely to be a debugger
def ParentAntiDebug():
    try:
        # Get the current process handle
        current_process = ctypes.windll.kernel32.GetCurrentProcess()
        
        # Query the parent process information using NtQueryProc
        proc_info = NtQueryProc(current_process, 0)
        
        # Get a handle to the parent process
        parent_process = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, proc_info.InheritedFromUniqueProcessId)
        if not parent_process:
            raise ctypes.WinError(ctypes.get_last_error())
        
        # Get the parent process name
        parent_process_name = QueryImageName(parent_process)
        
        # Close the handle to the parent process
        ctypes.windll.kernel32.CloseHandle(parent_process)
        
        # Check if the parent process is a known system process (likely benign)
        if not (parent_process_name.endswith("explorer.exe") or parent_process_name.endswith("cmd.exe")):
            return True  # Parent process is suspicious (not explorer or cmd)
        else:
            return False  # Parent process is benign (explorer or cmd)
    
    except Exception as e:
        # Handle any errors and return False if something goes wrong
        print(f"Error: {e}")
        return False

# IMPORTANT NOTES:
# This function is designed to check if the parent process is likely to be a debugger or monitoring tool.
# - It checks for parent processes that are commonly associated with legitimate system operations, such as "explorer.exe" or "cmd.exe".
# - If the parent process is not one of these, it may indicate the presence of a debugger or tampering tool.
# - The function raises exceptions if any issues occur while querying process information or interacting with system resources.
#
# USE CAUTION: The use of this function is intended for debugging or system administration purposes. It can help in detecting debugger environments that could be used for reverse engineering or tampering.
