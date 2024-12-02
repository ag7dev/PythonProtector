import ctypes

# Load the necessary kernel32 library functions from Windows
kernel32 = ctypes.windll.kernel32

def CheckRemoteDebugger():
    try:
        # Get the current process handle
        process_handle = kernel32.GetCurrentProcess()
        
        # Create a variable to store whether a remote debugger is detected
        is_debugger_detected = ctypes.c_int(0)
        
        # Check if a remote debugger is present on the current process
        kernel32.CheckRemoteDebuggerPresent(process_handle, ctypes.byref(is_debugger_detected))
        
        # Return True if debugger is detected, False otherwise
        return is_debugger_detected.value != 0
    
    except Exception as e:
        # Handle any errors that occur during the process
        print(f"Error checking for remote debugger: {e}")
        return False
