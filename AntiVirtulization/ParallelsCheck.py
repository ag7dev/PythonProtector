import os
import glob

def CheckForParallels():
    # List of known Parallels drivers that are typically used by the Parallels virtual machine software
    parallels_drivers = ["prl_sf", "prl_tg", "prl_eth"]
    
    # Get the System32 folder path from the system environment
    sys32_folder = os.path.join(os.getenv("SystemRoot", ""), "System32")

    try:
        # List all files in the System32 directory
        files = os.listdir(sys32_folder)
        
        # Check if any of the Parallels driver files are present
        for file in files:
            for driver in parallels_drivers:
                if driver in file.lower():
                    return True, None  # Parallels-related drivers found
        
    except Exception as e:
        # Handle any errors that occur when accessing the System32 directory
        return False, f"Error accessing System32 directory: {e}"

    # If no Parallels drivers are found, return False
    return False, None


# IMPORTANT NOTICE:
# This function checks for the presence of Parallels virtual machine drivers (e.g., "prl_sf", "prl_tg", "prl_eth")
# in the System32 directory, which may indicate that the system is running in a Parallels virtual machine.
#
# Keep the following in mind:
# - This check is intended to detect Parallels-related drivers. Other virtualization platforms may not be detected.
# - The driver names used here are specific to Parallels and may vary depending on the version.
#
# This function should be used responsibly and in a controlled environment, particularly if used for detecting virtual environments.
# Avoid using it to bypass security measures or for malicious purposes.
