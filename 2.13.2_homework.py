
print(b'\xe7\x9f\xa5\xe8\xa1\x8c\xe5\x90\x88\xe4\xb8\x80'.decode('utf-8'))
a = b'\xe7\x9f\xa5\xe8\xa1\x8c\xe5\x90\x88\xe4\xb8\x80'.decode('utf-8')
print(a)

file1 = open(r'document_1601.txt','w')
file1.write(b'\xe7\x9f\xa5\xe8\xa1\x8c\xe5\x90\x88\xe4\xb8\x80'.decode('utf-8'))
file1.close()

# 复习今天所学的内容，编码、解码与文件读写，完成下面题目
#
# 第二步:分析过程
# 在practice_1602.py文件中，可以接收用户所输入的任何内容，在这内容前面加上“您输入的是：”; 之后将所有的内容写入到document_1602.txt文件中。
a = input("请输入内容:")
file2 = open(r'document_1602.txt','w')
file2.write("您输入的是：" + a)
file2.close()
