import json
import subprocess
import argparse
import os
import sys

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate font files from glyph data.')
    parser.add_argument("--json-file", required=True, help="Path to the JSON file containing glyph data.")
    parser.add_argument("--bbp", type=int, required=True, help="Bits per pixel for the font.")
    parser.add_argument("--font-name", required=True, help="Name of the font.")
    parser.add_argument("--font-sizes", type=int, required=True, nargs='+', help="List of font sizes to generate.")
    args = parser.parse_args()

    # Check if JSON file exists
    if not os.path.isfile(args.json_file):
        print(f"Error: JSON file '{args.json_file}' not found.")
        sys.exit(1)

    # Read and parse the JSON file
    with open(args.json_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
            sys.exit(1)

    # Extract and process unicode values
    try:
        unicode_strings = [glyph['unicode'] for glyph in data['glyphs']]
    except KeyError:
        print("Error: JSON data does not contain 'glyphs' key or 'unicode' values.")
        sys.exit(1)

    # Convert unicode strings to decimal integers
    code_points = []
    for u in unicode_strings:
        code_points.append("0x"+u)

    # Determine the minimum and maximum code points
    if not code_points:
        print("No valid code points found.")
        sys.exit(1)


    # Format the RANGE string
    RANGE = ','.join(code_points)
    print(f"RANGE: {RANGE}")

    # Loop through each font size and generate the font files
    for font_size in args.font_sizes:
        # Construct the command
        command = [
            "lv_font_conv",
            f"--font {args.font_name}.ttf",
            f"-r {RANGE}",
            "--no-compress",
            f"--size {font_size}",
            "--format lvgl",
            f"--bpp {args.bbp}",
            f"-o {args.font_name}_{font_size}.c"
        ]
        command_str = " ".join(command)
        
        # Execute the command
        try:
            subprocess.run(command_str, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            continue
        
        # Print the font declaration
        print(f"LV_FONT_DECLARE({args.font_name}_{font_size})")

if __name__ == "__main__":
    main()