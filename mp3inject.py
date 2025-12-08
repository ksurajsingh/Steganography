import sys
import struct

#! Python for injecting data inside an MP3 using EOF steganography

if len(sys.argv) != 4:
    print("Usage: python <prgm_name> <input_audio> <input_secret> <output_audio>")
    sys.exit(1)

input_audio = sys.argv[1]
input_secret = sys.argv[2]
output_audio = sys.argv[3]

with open(input_audio, 'rb') as f, open(input_secret, 'rb') as e, open(output_audio, 'wb') as out:
    original_data = f.read()
    secret_data = e.read()
    
    # Write: [Original File][Secret Data][Size (8 bytes)]
    out.write(original_data)
    out.write(secret_data)
    # Append the original file size as 8-byte little-endian integer
    out.write(struct.pack('<Q', len(original_data)))

