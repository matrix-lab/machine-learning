with open('my_path/my_file.text', 'r') as f:
     file_data = f.read()

print(file_data)
# with 使用次关键字打开文件能够自动关闭读写流文件