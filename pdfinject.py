import sys

#! Python for injecting data inside a PDF using EOF steganography

if len(sys.argv) != 4:
    print("Usage: python <prgm_name> <input_pdf> <input_secret> <output_pdf>")
    sys.exit(1)

input_pdf = sys.argv[1]
input_secret = sys.argv[2]
output_pdf = sys.argv[3]

with open(input_pdf, 'rb') as f, open(input_secret, 'rb') as e, open(output_pdf, 'wb') as out:
    out.write(f.read() + e.read())

