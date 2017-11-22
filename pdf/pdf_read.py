# encoding:utf-8
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# 以二进制形式打开
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

fp.close()