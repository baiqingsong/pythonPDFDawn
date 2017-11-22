# python 解析PDF文件

* [插件](#插件)
* [pdf读取](#pdf读取)
* [txt读取](#txt读取)
* [读取文件模式](#读取文件模式)

## 插件
[https://pypi.python.org/pypi/pdfminer/](https://pypi.python.org/pypi/pdfminer/)  
需要下载pdfminer插件，如果python3的用户需要下载pdfminer3k  
解压文件，找到setup.py文件位置，命令行安装pdfminer  
python setup.py install  

## pdf读取
1. 创建文本分析器
2. 创建文本对象
3. 创建资源管理器
4. 创建LA分析
5. 创建设备对象，并将资源管理器对象和LA分析对象传入，注意第二个参数要写（laparams=）
6. 创建一个解释器对象，并将资源管理器对象和设备对象传入
7. 遍历文档对象的总页数
8. 处理每一页的内容
```
# encoding:utf-8
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

fp = open('simple1.pdf', 'rb')

# 创建一个pdf文档分析器
parser = PDFParser(fp)

# 创建一个PDF文档对象储存文档结构
document = PDFDocument(parser)

# 检查文件是否允许文本提取
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # 创建一个PDF资源管理器对想来存储共同资源
    rsrcmgr = PDFResourceManager()

    # 设定参数进行分析
    laparams = LAParams()

    # 创建一个PDF设备对象
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)

    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # 遍历文档对象的总页数
    for page in PDFPage.create_pages(document):
        # 解析每一页
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        for x in layout:
            if hasattr(x, 'get_text'):
                print x.get_text().encode('utf-8')
```

## txt读取
txt文件的读取比较简单，直接打开文件，然后调用read()方法即可
```
f = open('demo.txt')
print f.read()
```

## 读取文件模式
open方法读取文件模式有多种  
`w`                       以写的方式打开，默认  
`a`                       以追加的模式打开（从EOF开始，必要时创建文件）  
`r+`                      以读写的方式打开  
`w+`                      以读写的方式打开  
`a+`                      以读写的方式打开  
`rb`                      以二进制读的方式打开  
`wb`                      以二进制写的方式打开  
`ab`                      以二进制追加的方式打开  
`rb+`                     以二进制读写的方式打开  
`wb+`                     以二进制读写的方式打开  
`ab+`                     以二进制读写的方式打开  

注意：
1. 使用`w`,文件若存在，首先先清空，然后（重新）创建。
2. 使用`a`模式，把所有要写入文件的数据都追加到文件的末尾，即使使用了seek()方法指向文件的其他地方。如果文件不存在，将自动被创建
3. 使用open打开文件后一定要记得关闭文件对象f.close()。可以用finally关闭