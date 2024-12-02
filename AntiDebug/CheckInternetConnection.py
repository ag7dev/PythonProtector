import socket

def check_connection():
    try:
        # Attempt to create a connection to google.com on port 80 (HTTP)
        socket.create_connection(("google.com", 80), timeout=5)
        return True, None  # Return True if the connection is successful
    except socket.error as ex:
        # If a connection error occurs, capture the exception and print a debug message
        error_message = f"Error checking internet connection: {ex}"
        print(f"[DEBUG] {error_message}")
        # Return False with the exception message to indicate the failure
        return False, Exception(error_message)

# IMPORTANT NOTICE:
# This function attempts to establish a socket connection to "google.com" on port 80 (HTTP) with a timeout of 5 seconds.
# It is used to check the availability of an internet connection by trying to reach a known, reliable external server.
#
# Key points to consider:
# - A successful connection implies that the system has internet access.
# - If the connection fails, the function will raise an exception with the error details.
# - The timeout is set to 5 seconds, but this can be adjusted depending on network conditions.
#
# Use this function responsibly:
# - This function should be used to check basic internet connectivity and is not intended for diagnostic or monitoring purposes beyond that.
# - Avoid using this function in production code without proper error handling and logging mechanisms in place