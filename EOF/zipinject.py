import sys

#! Python for injecting data inside a ZIP using EOF steganography

if len(sys.argv) != 4:
    print("Usage: python <prgm_name> <input_zip> <input_secret> <output_zip>")
    sys.exit(1)

input_zip = sys.argv[1]
input_secret = sys.argv[2]
output_zip = sys.argv[3]

with open(input_zip, 'rb') as f, open(input_secret, 'rb') as e, open(output_zip, 'wb') as out:
    out.write(f.read() + e.read())

