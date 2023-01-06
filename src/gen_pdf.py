"""
    Created by howie.hu at 2021-12-31.
    Description: 周刊生成PDF https://github.com/simonhaenisch/md-to-pdf
        - 命令：npm i -g md-to-pdf
        - md2pdf ./archive/2021/2021_header.md  --config-file ./src/config.json
        - "~/Documents/programming/weekly/src/statics/pdf.css"

    Changelog: all notable changes to this file will be documented
"""
import os
import subprocess

from PyPDF2 import PdfFileReader, PdfFileWriter


def gen_pdf(years: int, force_pdf: bool = True):
    """生成pdf命令
    没有pdf就生成，生成的就合并
    Args:
        years (int): 年份
        force_pdf (bool, optional): [description]. Defaults to True.
    """
    root_path = os.path.dirname(os.path.dirname(__file__))
    target_path = os.path.join(root_path, f"docs/{years}")
    all_pdfs = []
    for _file in os.listdir(target_path):
        if str(_file).endswith(".md"):
            file_path = os.path.join(target_path, _file)
            pdf_file_path = file_path.replace(".md", ".pdf")
            if os.path.exists(pdf_file_path) and not force_pdf:
                print(f"{pdf_file_path} 已存在，不用生成")
            else:
                cmd = f"md2pdf {file_path} --config-file {root_path}/src/config.json"
                print(f"{pdf_file_path} 生成中...")
                res = subprocess.call(cmd, shell=True)
                print(f"{cmd} \n 命令执行结果: {res}")

            all_pdfs.append(pdf_file_path)
    all_pdfs.sort()
    pdf_writer = PdfFileWriter()

    bookmark_dict = {}
    all_pages = 0
    for pdf_path in all_pdfs:
        chapter_name = str(pdf_path).split("/")[-1].split(".pdf")[0]
        print(chapter_name)
        bookmark_dict[chapter_name] = all_pages
        pdf_reader = PdfFileReader(pdf_path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
        all_pages += pdf_reader.getNumPages()

    for bookmark, page in bookmark_dict.items():
        pdf_writer.addBookmark(bookmark, page)

    with open(f"./{years}_老胡的周刊.pdf", "wb") as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    gen_pdf(years=2022, force_pdf=True)
