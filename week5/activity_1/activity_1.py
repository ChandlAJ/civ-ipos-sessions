import codecs

def reverse_bytes(bytes_data):
    return bytes_data[::-1]

def convert_bytes_to_text(bytes_data):
    return bytes_data.decode('utf-8')

def convert_text_to_bytes(text_data):
    return text_data.encode('utf-8')

def main():
    try:
        # Open the binary file for reading and create output files for writing
        with open("data.bin", "rb") as binaryfile, \
             open("converted_text.txt", "w", encoding="utf-8") as text_out, \
             open("reversed_bytes.bin", "wb") as bytes_out:

            # Iterate through each line in the binary file
            for line in binaryfile:
                try:
                    # Decode the line to Unicode string and remove leading/trailing whitespaces
                    decoded_line = line.decode('utf-8').strip()

                    # Check if the line starts with "TEXT:"
                    if decoded_line.startswith("TEXT:"):
                        content = decoded_line[5:].strip()
                        upper_text = content.upper()
                        text_out.write(upper_text + "\n")

                    # Check if the line starts with "BYTES:"
                    elif decoded_line.startswith("BYTES:"):
                        hex_string = decoded_line[6:].strip()
                        try:
                            byte_data = codecs.escape_decode(hex_string)[0]
                            reversed_data = reverse_bytes(byte_data)
                            bytes_out.write(reversed_data + b"\n")
                        except ValueError:
                            print(f"⚠️ Invalid hex string: {hex_string}")

                except UnicodeError:
                    print("⚠️ Skipping undecodable line:", line)

        print("✅ Processing complete. Files saved.")

    except IOError as io_error:
        print("❌ File I/O error occurred:", io_error)

    except Exception as exception:
        print("❌ Unexpected error occurred:", exception)

if __name__ == "__main__":
    main()