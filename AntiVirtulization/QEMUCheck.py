import os

def CheckForQEMU():
    # List of known QEMU-related drivers that are used by the QEMU virtualization platform
    qemu_drivers = ["qemu-ga", "qemuwmi"]
    
    # Get the System32 folder path from the system environment
    sys32 = os.path.join(os.getenv("SystemRoot", ""), "System32")

    try:
        # List of detected QEMU drivers
        detected_drivers = []
        
        # List all files in the System32 directory
        files = os.listdir(sys32)
        
        # Check if any of the QEMU-related drivers are present
        for file in files:
            for driver in qemu_drivers:
                if driver in file.lower():
                    detected_drivers.append(driver)
        
        # Return True and the detected drivers if any are found
        if detected_drivers:
            return True, detected_drivers
        
        # Return False if no QEMU drivers are detected
        else:
            return False, None
    
    except Exception as e:
        # Handle any errors that occur while accessing the System32 directory
        return False, f"Error accessing System32 directory: {e}"

    # Default return if no QEMU drivers are detected
    return False, None


# IMPORTANT NOTICE:
# This function checks the System32 directory for the presence of QEMU-specific drivers (e.g., "qemu-ga", "qemuwmi"),
# which can indicate that the system is running in a QEMU virtual machine.
#
# Key points to consider:
# - The driver names listed here are common for QEMU but might vary depending on the version of QEMU being used.
# - This check is specifically designed to detect QEMU-related drivers and may not detect other virtualization platforms.
#
# Use this function with caution:
# - It's important to only use this check in a responsible manner, ensuring it is not used for any malicious activities
#   or to bypass virtual machine detection inappropriately.
# - Be aware that this check may not be foolproof and can be bypassed by sophisticated virtual