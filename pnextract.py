import sys

#! Python to extract text from PNG

if len(sys.argv) != 3:  
    print("Usage: python <prgm_name> <input_file> <output_file>")
    sys.exit(1)

input_file=sys.argv[1]
output_file=sys.argv[2]

with open (input_file,'rb') as f:
    content=f.read()
    offset=content.rindex(bytes.fromhex('49 45 4E 44 AE 42 60 82'))
    f.seek(offset+8)

    with open(output_file,'wb') as w:
        w.write(f.read())
