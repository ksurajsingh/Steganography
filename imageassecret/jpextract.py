import sys

#! Python to extract text from JPEG

if len(sys.argv) != 3:  
    print("Usage: python <prgm_name> <input_file> <output_file>")
    sys.exit(1)

input_file=sys.argv[1]
output_file=sys.argv[2]

with open (input_file,'rb') as f:
    content=f.read()
    offset=content.rindex(bytes.fromhex('FFD9'))
    offset2=content.rindex(bytes.fromhex('FFD9'),0,offset)
    f.seek(offset2+2)

    with open(output_file,'wb') as w:
        w.write(f.read())
