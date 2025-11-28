import sys
from PIL import Image
import struct

#! Python to extract data from JPEG using LSB steganography
# Note: JPEG is lossy, so extraction may be less reliable than PNG

if len(sys.argv) != 3:
    print("Usage: python <prgm_name> <input_image> <output_file>")
    sys.exit(1)

input_image = sys.argv[1]
output_file = sys.argv[2]

# Open the stego image
img = Image.open(input_image)
if img.mode != 'RGB':
    img = img.convert('RGB')

width, height = img.size
pixels = img.load()

# Extract LSBs from pixels
extracted_bits = []
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        extracted_bits.append(str(r & 1))
        extracted_bits.append(str(g & 1))
        extracted_bits.append(str(b & 1))

# Convert bits to bytes
bit_string = ''.join(extracted_bits)

# First 32 bits (4 bytes) contain the size of the secret file
size_bits = bit_string[:32]
size_bytes = bytes(int(size_bits[i:i+8], 2) for i in range(0, 32, 8))
secret_size = struct.unpack('<I', size_bytes)[0]

# Calculate how many bits we need (size header + secret data)
total_bits_needed = 32 + (secret_size * 8)

if total_bits_needed > len(bit_string):
    print(f"Error: Not enough data extracted. Expected {total_bits_needed} bits, got {len(bit_string)}")
    sys.exit(1)

# Extract the secret data bits
secret_bits = bit_string[32:total_bits_needed]

# Convert bits to bytes
secret_bytes = bytes(int(secret_bits[i:i+8], 2) for i in range(0, len(secret_bits), 8))

# Write the extracted secret
with open(output_file, 'wb') as f:
    f.write(secret_bytes)

print(f"Successfully extracted {secret_size} bytes to {output_file}")
print("Note: JPEG is lossy - extraction may have errors")

