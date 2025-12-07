import sys
import struct

#! Python for injecting data inside an MP4 using EOF steganography

if len(sys.argv) != 4:
    print("Usage: python <prgm_name> <input_video> <input_secret> <output_video>")
    sys.exit(1)

input_video = sys.argv[1]
input_secret = sys.argv[2]
output_video = sys.argv[3]

with open(input_video, 'rb') as f, open(input_secret, 'rb') as e, open(output_video, 'wb') as out:
    original_data = f.read()
    secret_data = e.read()
    
    # Write: [Original File][Secret Data][Size (8 bytes)]
    out.write(original_data)
    out.write(secret_data)
    # Append the original file size as 8-byte little-endian integer
    out.write(struct.pack('<Q', len(original_data)))

