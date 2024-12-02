import ctypes

# Access kernel32.dll to use GetTickCount function
kernel32 = ctypes.windll.kernel32
getTickCount = kernel32.GetTickCount
getTickCount.restype = ctypes.c_ulong  # Specify the return type of the function

def GetUptimeInSeconds():
    try:
        # Get the system uptime in milliseconds
        uptime = getTickCount()
        # Convert uptime from milliseconds to seconds and return as integer
        return int(uptime / 1000)
    except Exception as e:
        # If an error occurs during the function call, handle it
        print(f"[DEBUG] Error in GetUptimeInSeconds: {e}")
        return 0

def CheckUptime(durationInSeconds):
    try:
        # Get the current system uptime in seconds
        uptime = GetUptimeInSeconds()
        # Compare the uptime with the given duration
        if uptime < durationInSeconds:
            return True, None  # System has been up for less than the specified duration
        else:
            return False, None  # System has been up for longer than the specified duration
    except Exception as e:
        # Handle any errors that occur during the uptime check
        print(f"[DEBUG] Error in CheckUptime: {e}")
        return False, f"Error in uptime check: {e}"

# IMPORTANT NOTICE:
# The GetUptimeInSeconds function retrieves the system uptime (time since boot) in seconds by calling the GetTickCount function from kernel32.dll.
# The CheckUptime function checks if the system has been running for less than the specified duration in seconds.
#
# Key points to consider:
# - GetUptimeInSeconds returns the uptime in seconds by converting the value from milliseconds.
# - If there are any errors accessing the uptime or performing the comparison, the error is handled and logged.
# - This function is useful for detecting if the system has been up for a specific duration or for uptime-related checks.
#
# Use this function responsibly:
# - Ensure that this function is used in contexts where system uptime is relevant (e.g., process monitoring, system diagnostics).
# - Be aware of potential issues with system uptime measurement, such as changes in system clock or uptime