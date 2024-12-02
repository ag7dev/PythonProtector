import ctypes

# Access the kernel32.dll to use the IsDebuggerPresent function
kernel32 = ctypes.windll.kernel32

def is_debugger_present():
    try:
        # Check if a debugger is attached to the process using IsDebuggerPresent
        # The function returns a non-zero value if a debugger is present
        return kernel32.IsDebuggerPresent() != 0
    except Exception as e:
        # Handle any errors that may occur when calling the function
        print(f"[DEBUG] Error in is_debugger_present: {e}")
        return False  # Return False if there is an error checking for a debugger

# IMPORTANT NOTICE:
# The is_debugger_present function checks whether a debugger is currently attached to the process
# by calling the IsDebuggerPresent function from kernel32.dll.
# It returns True if a debugger is present, and False otherwise.
#
# Key points to consider:
# - A debugger is typically used for debugging programs, but it can also be used for reverse engineering or malicious activities.
# - This function can be useful for anti-debugging measures, as it detects when a debugger is attached.
#
# Use this function responsibly:
# - It is intended for use in security-related scenarios where the presence of a debugger needs to be detected (e.g., in malware protection or anti-tampering).
# - Avoid using this function in ways that could harm the user's system or violate privacy.
