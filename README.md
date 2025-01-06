# AliIcon2CHeader

## 项目介绍

AliIcon2CHeader 是一个将阿里巴巴矢量图标库导出的JSON文件转换为C语言头文件的工具。它能够自动将Unicode编码转换为UTF-8字符串，并生成宏定义，其名称采用中文拼音大写加下划线格式。

## 特点

- **自动转换**：自动将Unicode编码转换为UTF-8字符串。
- **命名规范**：宏定义名称采用中文拼音大写加下划线格式。
- **简单易用**：只需一条命令即可生成头文件。

## 安装

确保你已经安装了Python 3和pip，然后安装依赖库：

```bash
pip install pypinyin
```

## 使用方法

在命令行中运行脚本：

```bash
python icon2cheader.py input.json output.h
```

其中：

- `input.json` 是阿里巴巴矢量图标库导出的JSON文件。
- `output.h` 是生成的C头文件。

## 示例

假设有以下JSON文件`iconfont.json`：
```json
{
  "glyphs": [
    {
      "name": "多云",
      "unicode": "e600"
    },
    {
      "name": "晴",
      "unicode": "e6f5"
    }
  ]
}
```

运行命令：

```bash
python icon2cheader.py iconfont.json icons.h
```

生成的`icons.h`内容如下：
```C
#ifndef ICONS_H
#define ICONS_H

/* 多云 Unicode:e600 */
#define DUO_YUN "\xEE\x98\x80"

/* 晴 Unicode:e6f5 */
#define QING "\xEE\x9C\xB5"

#endif /* ICONS_H */
```



# AliIconFontGen：嵌入式系统自定义图标字体生成工具


## 项目概述
AliIconFontGen 是一个开源工具，专为嵌入式系统中使用的 LVGL（轻量且 versatile 的图形库）自动生成自定义字体。该工具通过处理阿里巴巴矢量图标库导出的JSON文件，输入文件中的字符数据，生成适用于 LVGL 的字体文件，提供灵活性以适应不同的字体大小和位深度（BPP）设置。

## 主要特点

* 数据智能解析：从JSON 输入文件中自动确定 Unicode ，无需手动配置。
* 多字体大小和 BPP 支持：支持生成不同大小和 BPP 设置的字体，以满足不同的显示需求。
* 命令行接口：易于集成到构建管道或脚本中。
* 健壮的错误处理：包含 comprehensive 的错误检查，确保文件存在、JSON 解析和无效 Unicode 值等问题。


安装与使用
### 依赖
确保 lv_font_conv 已安装并包含在系统 PATH 中。

Python 脚本无需额外安装，仅使用标准库。

### 使用说明
通过命令行参数指定 JSON 文件、BPP、字体名称和字体大小来运行脚本。

### 示例：
```bash
python iconfontgen.py --json-file iconfont.json --bbp 1 --font-name iconfont --font-sizes 14 36
```

## JSON 文件格式
输入的 JSON 文件应包含一组字符，每个字符具有一个 unicode 值。示例结构如下：

```json
{
    "glyphs": [
        { "name": "glyph1", "unicode": "0xe6f7" },
        { "name": "glyph2", "unicode": "0xe700" },
        { "name": "glyph3", "unicode": "0xe600" }
    ]
}
```


## 贡献

欢迎提交Issue和Pull Request来改进这个工具。

## 许可证

本项目采用 Apache License 2.0 许可证。详细内容请参见 [LICENSE](LICENSE) 文件。
