import sys
from PIL import Image
import struct

#! Python for injecting data inside a PNG using LSB steganography

if len(sys.argv) != 4:
    print("Usage: python <prgm_name> <input_image> <input_secret> <output_image>")
    sys.exit(1)

input_image = sys.argv[1]
input_secret = sys.argv[2]
output_image = sys.argv[3]

# Open the cover image
img = Image.open(input_image)
if img.mode != 'RGB':
    img = img.convert('RGB')

width, height = img.size
pixels = img.load()

# Read the secret file
with open(input_secret, 'rb') as f:
    secret_data = f.read()

# Calculate capacity: 3 bits per pixel (RGB), minus 32 bits for size header
max_capacity = (width * height * 3) // 8 - 4
if len(secret_data) > max_capacity:
    print(f"Error: Secret file too large. Maximum capacity: {max_capacity} bytes")
    print(f"Secret file size: {len(secret_data)} bytes")
    sys.exit(1)

# Convert secret data to binary string
secret_bits = ''.join(format(byte, '08b') for byte in secret_data)

# Add size header (4 bytes = 32 bits) to indicate secret file size
size_header = struct.pack('<I', len(secret_data))
size_bits = ''.join(format(byte, '08b') for byte in size_header)

# Combine size header and secret data
all_bits = size_bits + secret_bits

# Embed the bits into the image
bit_index = 0
for y in range(height):
    for x in range(width):
        if bit_index >= len(all_bits):
            break
        
        r, g, b = pixels[x, y]
        
        # Modify LSB of each channel
        if bit_index < len(all_bits):
            r = (r & 0xFE) | int(all_bits[bit_index])
            bit_index += 1
        if bit_index < len(all_bits):
            g = (g & 0xFE) | int(all_bits[bit_index])
            bit_index += 1
        if bit_index < len(all_bits):
            b = (b & 0xFE) | int(all_bits[bit_index])
            bit_index += 1
        
        pixels[x, y] = (r, g, b)
    
    if bit_index >= len(all_bits):
        break

# Save the stego image
img.save(output_image, 'PNG')
print(f"Successfully embedded {len(secret_data)} bytes into {output_image}")

