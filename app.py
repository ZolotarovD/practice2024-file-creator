import os
import sys
import codecs

def create_file(file_name):
    with open(file_name, 'w') as f:
        f.write('')

def list_files(directory):
    return os.listdir(directory)

def read_file(file_name):
    with open(file_name, 'rb') as f:
        raw_data = f.read()
        for bom, encoding in (
            (codecs.BOM_UTF8, 'utf-8'),
            (codecs.BOM_UTF16, 'utf-16'),
            (codecs.BOM_UTF16_BE, 'utf-16-be'),
            (codecs.BOM_UTF16_LE, 'utf-16-le'),
            (codecs.BOM_UTF32, 'utf-32'),
            (codecs.BOM_UTF32_BE, 'utf-32-be'),
            (codecs.BOM_UTF32_LE, 'utf-32-le'),
        ):
            if raw_data.startswith(bom):
                return raw_data[len(bom):].decode(encoding)
        return raw_data.decode('latin-1')

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "read":
        content = read_file(sys.argv[2])
        print(content)
    elif len(sys.argv) > 1:
        create_file(sys.argv[1])
    else:
        files = list_files('.')
        for file in files:
            print(file)
