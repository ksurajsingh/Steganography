import sys

#! Python for injecting text inside a JPEG 

if len(sys.argv)!=4:
   print("Usage: python <prgm_name> <input_image> <input_text> <output_image>")
   sys.exit(1)

input_image=sys.argv[1]
input_text=sys.argv[2]
output_image=sys.argv[3]

with open (input_image,'rb') as f   , open (input_text,'rb') as e, open(output_image,'wb') as out:

   out.write(f.read()+e.read())