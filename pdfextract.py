import sys

#! Python to extract data from PDF using EOF steganography

if len(sys.argv) != 3:
    print("Usage: python <prgm_name> <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'rb') as f:
    content = f.read()
    
    # PDF ends with %%EOF (may have whitespace/newlines before it)
    # Look for the last occurrence of %%EOF
    eof_marker = b'%%EOF'
    offset = content.rfind(eof_marker)
    
    if offset == -1:
        print("Error: Could not find %%EOF marker in PDF")
        sys.exit(1)
    
    # Find the end of the line containing %%EOF
    # PDF spec allows whitespace after %%EOF
    end_pos = offset + len(eof_marker)
    
    # Skip any whitespace/newlines after %%EOF
    while end_pos < len(content) and content[end_pos] in b' \t\n\r':
        end_pos += 1
    
    f.seek(end_pos)
    
    with open(output_file, 'wb') as w:
        w.write(f.read())

