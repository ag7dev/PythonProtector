import subprocess

def PluggedIn():
    try:
        # Run the registry query to check for USB storage devices
        usbcheckcmd = subprocess.Popen(
            ['reg', 'query', 'HKLM\\SYSTEM\\ControlSet001\\Enum\\USBSTOR'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
        )
        
        # Get the output and error from the command
        outputusb, err = usbcheckcmd.communicate()
        
        # If there's an error, return False indicating no USB storage detected
        if err:
            return False

        # Decode the output and split it into lines
        usblines = outputusb.decode('utf-8').split("\n")
        
        # Count how many USB storage devices are plugged in
        pluggedusb = 0
        for line in usblines:
            if line.strip().startswith("HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Enum\\USBSTOR"):
                pluggedusb += 1
        
        # If any USB storage devices are found, return True
        if pluggedusb > 0:
            return True
        else:
            return False

    except Exception as e:
        # Handle any errors that occur during the execution of the command
        print(f"Debug Check: Error running reg query command: {e}")
        return False


# IMPORTANT NOTICE:
# This function checks the Windows registry to see if any USB storage devices are currently plugged in.
# It queries the registry location `HKLM\\SYSTEM\\ControlSet001\\Enum\\USBSTOR`, which stores information about connected USB storage devices.
#
# Key points to consider:
# - The function relies on the registry to detect plugged-in USB storage devices, so it may not detect devices that do not appear in the registry.
# - The function counts any entries starting with "HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Enum\\USBSTOR", which typically corresponds to USB storage devices.
#
# Use this function responsibly:
# - This function should not be used to monitor users' device connections without their consent.
# - It requires administrative privileges to access certain registry locations, and its results may vary based on user access control settings.
