import os
import glob

def VMArtifactsDetect():
    # List of known VM-related file names (typically used by VirtualBox and VMware)
    bad_file_names = [
        "VBoxMouse.sys", "VBoxGuest.sys", "VBoxSF.sys", "VBoxVideo.sys", 
        "vmmouse.sys", "vboxogl.dll"
    ]
    
    # List of known directories associated with VMware and VirtualBox guest additions
    bad_dirs = [
        r'C:\Program Files\VMware', r'C:\Program Files\oracle\virtualbox guest additions'
    ]

    # System32 folder path
    system32_folder = os.getenv("SystemRoot", "") + r'\System32'
    
    try:
        # List all files in the System32 directory
        files = glob.glob(os.path.join(system32_folder, "*"))
    except Exception as e:
        # Handle any errors that occur while accessing the System32 folder
        print(f"Error accessing System32 folder: {e}")
        return False

    # Convert the list of bad file names to lowercase for case-insensitive comparison
    badfileslower = [name.lower() for name in bad_file_names]

    # Check if any of the files in System32 match the bad file names
    for file_path in files:
        file_name = os.path.basename(file_path).lower()
        if file_name in badfileslower:
            return True  # VM-related artifact found
    
    # Convert the list of bad directories to lowercase for case-insensitive comparison
    bad_dirs_lower = [dir.lower() for dir in bad_dirs]

    # Check if any of the bad directories exist on the system
    for bad_dir in bad_dirs_lower:
        if os.path.exists(bad_dir):
            return True  # VM-related directory found

    return False  # No VM artifacts detected


# IMPORTANT NOTICE:
# This function checks for the presence of specific files and directories that are commonly associated with virtual machines (VMs) like VirtualBox and VMware.
# It looks for known files (e.g., "VBoxMouse.sys") in the System32 directory and specific directories where VM guest additions are installed.
#
# Key points to consider:
# - The function scans for virtual machine artifacts commonly left behind by VirtualBox and VMware environments.
# - It checks for files and directories in a case-insensitive manner, ensuring it can detect artifacts regardless of case.
# - This method is useful for detecting certain virtual machine environments, but it may not catch all VMs (e.g., other platforms like QEMU or Hyper-V may not be detected).
#
# Use this function responsibly:
# - This function should not be used to monitor or interfere with users without consent.
# - The presence of these files and directories alone is not a definitive indicator of a VM, as they may also be found in non-VM environments if installed separately.
# - Always consider the context and potential implications before using this function in any application or scenario.<|eom_id|>