"""
    Created by howie.hu at 2023-01-18.
    Description: 爬取周刊网站生成周刊
    Changelog: all notable changes to this file will be documented
"""

import os

from pysitemap import crawler


def gen_sitemap(url="https://weekly.howie6879.com/", file_name="sitemap"):
    """
    生成 sitemap
    """
    crawler(
        url,
        out_file=os.path.join(
            os.path.dirname(os.path.dirname(__file__)), f"docs/{file_name}.xml"
        ),
        exclude_urls=[".pdf", ".jpg", ".db", ".css", ".js", ".ico"],
    )


if __name__ == "__main__":
    gen_sitemap(url="https://weekly.howie6879.com/", file_name="howie_sitemap")
