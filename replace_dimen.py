import chardet
import re
from pathlib import Path


def get_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    return encoding


def recursive_replace_directory(directory, pattern, replacement):
    directory = Path(directory)

    for path in directory.rglob('*'):  # 递归遍历目录中的所有文件和子目录
        if path.is_file() and path.suffix in {'.kt', '.xml'}:  # 仅处理 .kt 和 .xml 文件
            file_encoding = get_file_encoding(path)
            print("file = ", path, "file_encoding = ", file_encoding)
            if file_encoding == 'windows-1251': continue

            with open(path, 'r', encoding=file_encoding) as f:
                content = f.read()

                # 查找匹配项
                matches = pattern.finditer(content)
                for match in matches:
                    print(f"Found match in {path}: {match.group()}")

                new_content = pattern.sub(replacement, content)

            with open(path, 'w', encoding=file_encoding) as f:
                f.write(new_content)


if __name__ == '__main__':
    directory_to_process = 'C:\\Users\\KYE\\IdeaProjects\\BaQiangKuaSheng'

    # 修正正则表达式模式
    pattern = re.compile(r'(name=\"|@dimen/|R\.dimen\.)sp_(\d+)')

    # 修正替换规则，使用捕获组引用数字部分
    replacement = r'\1ks_dp_\2'

    recursive_replace_directory(directory_to_process, pattern, replacement)
