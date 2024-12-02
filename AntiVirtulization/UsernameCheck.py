import os

def CheckForBlacklistedNames():
    # List of blacklisted usernames that may indicate suspicious or unwanted accounts
    blacklisted_names = [
        "johnson", "miller", "malware", "maltest", "currentuser", 
        "sandbox", "virus", "john doe", "test user", "sand box", "wdagutilityaccount"
    ]
    
    # Get the current username from the environment variables and convert to lowercase for comparison
    current_username = os.getenv("USERNAME", "").lower()
    
    # Check if the current username is in the list of blacklisted names
    if current_username in blacklisted_names:
        return True  # Blacklisted username found
    
    # Return False if the username is not blacklisted
    return False


# IMPORTANT NOTICE:
# This function checks if the current username is in a predefined list of blacklisted names.
# It is typically used to identify suspicious or unwanted user accounts that may be indicative of malicious activity or testing environments.
#
# Key points to consider:
# - The list of blacklisted names includes common test usernames, suspicious account names, and generic names often used in malware or sandbox environments.
# - This check is case-insensitive, so it will match usernames regardless of case.
#
# Use this function responsibly:
# - The function should not be used to unfairly monitor or restrict legitimate users.
# - It is useful for detecting test or unwanted accounts, but should not be relied upon as the sole security measure.
