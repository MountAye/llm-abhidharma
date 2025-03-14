import opencc
from pathlib import Path

def convert_traditional_to_simplified(input_file, output_file):
    # Initialize the converter
    converter = opencc.OpenCC('t2s')  # Converts Traditional to Simplified
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        traditional_lines = f.readlines()
    
    # Process lines: convert, remove blank lines, and remove specific character
    simplified_lines = [converter.convert(line.replace('\u3000', '').strip()) for line in traditional_lines if line.strip()]
    
    # Write the converted text to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(simplified_lines))
    
    print(f"Conversion complete. Simplified text saved to {output_file}")

# Example usage
# convert_traditional_to_simplified('traditional.txt', 'simplified.txt')

for path_tw in Path("data/zh-TW").glob("*"):
    if Path.is_dir(path_tw):
        if not (Path("data/zh-CN")/(path_tw.name)).exists():
            Path.mkdir(Path("data/zh-CN")/(path_tw.name))
        for subpath_tw in path_tw.glob("*.txt"):
            subpath_cn = Path("data/zh-CN")/path_tw.name/subpath_tw.name
            convert_traditional_to_simplified(str(subpath_tw),str(subpath_cn))
    else:
        path_cn = Path("data/zh-CN")/path_tw.name
        convert_traditional_to_simplified(str(path_tw),str(path_cn))
