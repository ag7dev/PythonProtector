import ctypes

def IsScreenSmall():
    try:
        # Access the user32 library to get system metrics
        user32 = ctypes.windll.user32

        # Get screen width (index 0) and height (index 1)
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)

        # Check if screen dimensions are below the minimum threshold (800x600)
        is_small = width < 800 or height < 600
        return is_small, None
    
    except Exception as e:
        # Handle any errors that occur while checking screen size
        return False, f"Error checking screen size: {e}"


# IMPORTANT NOTICE:
# This function checks the screen resolution to determine if the screen is considered "small" (below 800x600).
# It may be useful for determining compatibility with applications that require higher screen resolutions.
#
# Be aware of the following:
# - This check only evaluates the current screen resolution and does not account for multiple displays or virtual setups.
# - The threshold of 800x600 may be outdated for modern applications, and it's recommended to adjust the resolution check if needed.
#
# Use this function responsibly, especially when making UI/UX decisions or customizing applications for different screen sizes.
