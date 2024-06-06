import os
import subprocess
import sys

def add_device(device_path):
    try:
        # Check if device is a valid ESP32 by running esptool.py read_mac
        output = subprocess.check_output(f"esptool.py --port {device_path} read_mac", shell=True, text=True)
        
        lines = output.splitlines()
        
        mac = ""
        port = device_path
        
        for line in lines:
            if "MAC: " in line:
                mac = line.split("MAC: ")[1]
                break
        
        if not mac:
            print("Not an ESP32 device.")
            return

        # Create symlink with pattern /dev/espXXXX
        id = mac.replace(':', '')
        symlink = f"/dev/esp{id[-4:]}"
        
        if not os.path.exists(symlink):
            os.symlink(port, symlink)
            print(f"Created symlink: {symlink} -> {port}")
        else:
            print(f"Symlink {symlink} already exists.")

    except subprocess.CalledProcessError as e:
        print(f"Error running esptool.py: {e}")
        print(f"Output: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def remove_device(device_path):
    try:
        # Remove the symlink if it exists
        symlinks = [f for f in os.listdir('/dev') if os.path.islink(os.path.join('/dev', f)) and os.path.realpath(os.path.join('/dev', f)) == device_path]
        
        for symlink in symlinks:
            os.remove(os.path.join('/dev', symlink))
            print(f"Removed symlink: /dev/{symlink}")

    except Exception as e:
        print(f"Unexpected error: {e}")

def change_device(device_path):
    try:
        # Check if device is a valid ESP32 by running esptool.py read_mac
        output = subprocess.check_output(f"esptool.py --port {device_path} read_mac", shell=True, text=True)
        
        lines = output.splitlines()
        
        mac = ""
        port = device_path
        
        for line in lines:
            if "MAC: " in line:
                mac = line.split("MAC: ")[1]
                break
        
        if not mac:
            print("Not an ESP32 device.")
            return

        # Create symlink with pattern /dev/espXXXX
        id = mac.replace(':', '')
        symlink = f"/dev/esp{id[-4:]}"
        
        if not os.path.exists(symlink):
            remove_device(device_path)
            add_device(device_path)
        else:
            print(f"Symlink {symlink} already exists.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error running esptool.py: {e}")
        print(f"Output: {e.output}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def remove_all_symlinks():
    try:
        # Remove all symlinks that start with /dev/esp
        symlinks = [f for f in os.listdir('/dev') if f.startswith("esp") and os.path.islink(os.path.join('/dev', f))]
        
        for symlink in symlinks:
            os.remove(os.path.join('/dev', symlink))
            print(f"Removed symlink: /dev/{symlink}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        remove_all_symlinks()
    elif len(sys.argv) == 2:
        device_path = sys.argv[1]
        action = ""
        remove_all_symlinks()
    elif len(sys.argv) == 3:
        device_path = sys.argv[1]
        action = sys.argv[2]
        
        if action == "add":
            add_device(device_path)
        elif action == "remove":
            remove_device(device_path)
        elif action == "change":
            change_device(device_path)
        else:
            print("Unknown action")
