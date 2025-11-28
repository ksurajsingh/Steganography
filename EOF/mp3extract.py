import sys
import struct
import os

#! Python to extract data from MP3 using EOF steganography
# Note: MP3 doesn't have a clear end marker, so we read the size from the end of the file

if len(sys.argv) != 3:
    print("Usage: python <prgm_name> <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'rb') as f:
    # Get file size
    f.seek(0, os.SEEK_END)
    file_size = f.tell()
    
    # Read the last 8 bytes to get the original file size
    if file_size < 8:
        print("Error: File too small to contain size information")
        sys.exit(1)
    
    f.seek(-8, os.SEEK_END)
    size_bytes = f.read(8)
    original_size = struct.unpack('<Q', size_bytes)[0]
    
    # Extract secret data: everything from original_size to 8 bytes before the end
    f.seek(original_size)
    secret_data = f.read(file_size - original_size - 8)
    
    with open(output_file, 'wb') as w:
        w.write(secret_data)

