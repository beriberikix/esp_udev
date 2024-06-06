
# ESP32 udev Symlink Manager

This tool manages unique device ports/paths on Linux for embedded development using ESP32 devices. It combines a udev rule and a Python script to create user-friendly symlinks for ESP32 devices based on their MAC addresses.

## Overview

The udev rule runs a Python script whenever a USB device is added, removed, or changed. The script checks if the device is an ESP32, retrieves its MAC address, and creates a symlink with a pattern of `/dev/espXXXX`, where `XXXX` is the last four digits of the MAC address. It also handles the removal of symlinks when the device is unplugged or changed.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/beriberikix/esp-udev.git
   cd esp32-udev
   ```

2. **Install `esptool.py`:**

   Ensure `esptool.py` is installed and accessible in your PATH. You can install it using pip:

   ```bash
   pip3 install esptool
   ```

3. **Copy the udev rule:**

   Copy the udev rule to the udev rules directory:

   ```bash
   sudo cp 99-esp32.rules /etc/udev/rules.d/
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

4. **Copy the Python script:**

   Copy the Python script to `/usr/local/bin/` and make it executable:

   ```bash
   sudo cp esp_udev.py /usr/local/bin/
   sudo chmod +x /usr/local/bin/esp_udev.py
   ```

## Usage

The script and udev rule handle device add, remove, and change actions automatically.

### Manually Running the Script

You can also run the script manually for testing purposes:

1. **Add Device:**

   ```bash
   python /usr/local/bin/esp_udev.py /dev/ttyUSB0 add
   ```

   Replace `/dev/ttyUSB0` with the actual device path of your ESP32.

2. **Remove Device:**

   ```bash
   python /usr/local/bin/esp_udev.py /dev/ttyUSB0 remove
   ```

   Replace `/dev/ttyUSB0` with the actual device path of your ESP32.

3. **Change Device:**

   ```bash
   python /usr/local/bin/esp_udev.py /dev/ttyUSB0 change
   ```

   Replace `/dev/ttyUSB0` with the actual device path of your ESP32.

4. **Remove All Symlinks:**

   Run the script without any arguments to remove all symlinks starting with `/dev/esp`:

   ```bash
   python /usr/local/bin/esp_udev.py
   ```

## License

This project is licensed under the Apache 2 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
