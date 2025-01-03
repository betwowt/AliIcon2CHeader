### 简介
这个工具读取阿里巴巴矢量图标库导出的JSON文件，解析其中的图标信息，并生成一个C语言头文件。头文件中包含了每个图标的UTF-8编码字符串的宏定义，且宏名是根据图标中文名称翻译成拼音并用大写字母和下划线表示。

### 特点
自动将Unicode编码转换为UTF-8字符串。

宏定义名称采用中文拼音大写加下划线格式。

简单易用，只需一条命令即可生成头文件。

### 安装
确保你已经安装了Python 3和pip。

安装依赖：

```bash
pip install pypinyin
```

使用方法
在命令行中运行脚本：


```bash
python script.py input.json output.h
```

其中：

input.json 是阿里巴巴矢量图标库导出的JSON文件。

output.h 是生成的C头文件。

示例
假设有以下JSON文件iconfont.json：

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
python script.py iconfont.json icons.h
```

生成的icons.h内容如下：

```c
#ifndef ICONS_H
#define ICONS_H

/* 多云 Unicode:e600 */
#define DUO_YUN "\xEE\x98\x80"

/* 晴 Unicode:e6f5 */
#define QING "\xEE\x9C\xB5"

#endif /* ICONS_H */
```
贡献
欢迎提交Issue和Pull Request来改进这个工具。

许可证
Apache License 2.0
