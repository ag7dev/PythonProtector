import os
import glob

def CheckForKVM():
    # List of known KVM-related driver files that can indicate virtualization
    bad_drivers_list = ["balloon.sys", "netkvm.sys", "vioinput*", "viofs.sys", "vioser.sys"]
    
    # Get the System32 folder path from the system environment
    system32_folder = os.path.join(os.getenv("SystemRoot", ""), "System32")

    # Check if any of the bad drivers are present in the System32 folder
    for driver in bad_drivers_list:
        files = glob.glob(os.path.join(system32_folder, driver))
        if files:
            # If any matching files are found, KVM or a similar hypervisor is likely present
            return True, "KVM or similar hypervisor detected due to bad drivers"

    # If no matching files are found, no hypervisor is detected
    return False, "No KVM or hypervisor-related drivers detected"


# IMPORTANT NOTICE:
# This function checks for the presence of KVM or similar virtualization technologies by detecting
# certain driver files typically used by hypervisors. These driver files (like "balloon.sys" or "netkvm.sys")
# may indicate that the system is running inside a virtual machine.
#
# This check is for educational purposes or for detecting virtual environments. It should be used responsibly:
# - Do not use this check for malicious activities or to bypass virtualization detection mechanisms.
# - This function may not detect all hypervisors and is primarily useful for detecting known KVM drivers.
#
# Use it in a controlled environment and make sure to respect legal and ethical boundaries when using it.
