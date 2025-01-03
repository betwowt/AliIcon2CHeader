# 版权所有 [2024] [betwowt]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# 除非适用法律要求或书面同意，软件根据许可证分发 "按原样"，无任何 warranties 或条件。

import json
import sys
import pypinyin

def chinese_to_macro(name):
    pinyin_list = pypinyin.lazy_pinyin(name, style=pypinyin.Style.NORMAL)
    macro_name = '_'.join(pinyin_list).upper()
    return macro_name

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("#ifndef ICONS_H\n")
        f.write("#define ICONS_H\n\n")
        
        for glyph in data['glyphs']:
            name = glyph['name']
            font_class = glyph['font_class']
            unicode_hex = glyph['unicode']
            
            code_point = int(unicode_hex, 16)
            char = chr(code_point)
            utf8_bytes = char.encode('utf-8')
            escaped = '\\x' + '\\x'.join(format(b, '02X') for b in utf8_bytes)
            
            macro_name = chinese_to_macro(name)
            f.write(f"/* {name} Unicode:{unicode_hex} */\n")
            f.write(f"#define {macro_name}\t \"{escaped}\"\n\n")
        
        f.write("#endif /* ICONS_H */\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.json output.h")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)