import ctypes

def set_process_critical():
    try:
        # Check if the user has admin privileges
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        
        if is_admin:
            # Enable the privilege to set the process as critical
            privilege_enabled = ctypes.c_bool()
            ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(privilege_enabled))

            # If privilege is enabled, mark the process as critical
            if privilege_enabled.value:
                ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0)
                return True 
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return False 

# IMPORTANT NOTICE: 
# This code is provided for educational purposes only. It should not be used for malicious activities.
# Enabling a process as critical can prevent the termination of this process, but be cautious:
# If this critical process interferes with other important processes (e.g., in a virtual machine),
# it may cause system instability, including crashes or a Blue Screen of Death (BSOD).
# Use this functionality responsibly and only in appropriate environments.





