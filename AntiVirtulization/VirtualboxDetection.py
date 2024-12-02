import subprocess

def GraphicsCardCheck():
    try:
        # Run the wmic command to get information about the video controller (graphics card)
        cmd = subprocess.Popen(
            ['wmic', 'path', 'win32_VideoController', 'get', 'name'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        
        # Get the output and error from the command
        gpu_output, err = cmd.communicate()

        # If there's an error executing the command, print the error message and return False
        if err:
            print(f"Error executing command: {err.decode('utf-8').strip()}")
            return False
        
        # Check if the output contains references to VirtualBox graphics (indicating the use of VirtualBox)
        if b"virtualbox" in gpu_output.lower():
            return True  # VirtualBox detected
        
        # If no VirtualBox reference is found, return False
        return False
    
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(f"Error in GraphicsCardCheck: {e}")
        return False


# IMPORTANT NOTICE:
# This function checks the graphics card information using the 'wmic' command to detect whether the system is running in a VirtualBox environment.
# It looks for the string "virtualbox" in the output of the video controller's name to make this determination.
#
# Key points to consider:
# - The function specifically checks for VirtualBox-related graphics card names. It may not detect other virtual machine environments (such as VMware or QEMU).
# - The check relies on the 'wmic' command, which may not be available or may behave differently on certain system configurations.
#
# Use this function responsibly:
# - This function is useful for detecting VirtualBox environments, but it should not be used for malicious or unauthorized activities.
# - It's important to ensure that the function is not used to evade security checks or bypass virtual environment detection.
