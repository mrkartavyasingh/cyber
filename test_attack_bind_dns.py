import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 53))  # Bind to all interfaces
    print("✅ DNS port (53) is now occupied. DNS resolution should fail.")
    input("Press Enter to release port 53...")
    sock.close()
except PermissionError:
    print("❌ Permission Denied. Please run this script with sudo or as Administrator.")
except OSError as e:
    print(f"❌ OSError: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
