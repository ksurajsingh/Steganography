import sys

#! Python to extract data from ZIP using EOF steganography

if len(sys.argv) != 3:
    print("Usage: python <prgm_name> <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'rb') as f:
    content = f.read()
    
    # ZIP file ends with End of Central Directory Record
    # Signature: 0x06054b50 (PK\x05\x06)
    eocd_marker = bytes.fromhex('50 4B 05 06')
    offset = content.rfind(eocd_marker)
    
    if offset == -1:
        print("Error: Could not find End of Central Directory Record in ZIP")
        sys.exit(1)
    
    # End of Central Directory Record is 22 bytes long
    # But we need to account for the ZIP64 locator which might come after
    # For simplicity, we'll extract after the EOCD record (22 bytes)
    # More robust: parse the EOCD to find the actual end
    eocd_size = 22
    
    # Check for ZIP64 End of Central Directory Locator (0x07064b50)
    zip64_locator = bytes.fromhex('50 4B 06 07')
    zip64_locator_pos = content.rfind(zip64_locator, 0, offset)
    
    if zip64_locator_pos != -1:
        # ZIP64 locator is 20 bytes, then there's the ZIP64 EOCD
        # For simplicity, extract after the regular EOCD
        extract_start = offset + eocd_size
    else:
        extract_start = offset + eocd_size
    
    f.seek(extract_start)
    
    with open(output_file, 'wb') as w:
        w.write(f.read())

