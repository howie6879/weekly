    """
Created by howie.hu at 2021-10-30.
Description: Weekly Newsletter Initialization Script
Changelog: All notable changes to this file will be documented
"""

import os
import re
import logging
import yaml
from src.db import parse_md
from src.gen_sitemap import gen_sitemap
from src.rss import gen_rss

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_mkdocs_config(path=""):
    """Reads the mkdocs configuration file."""
    config_path = path or os.path.join(os.path.dirname(__file__), "mkdocs.yml")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading configuration file: {e}")
        raise

def write_mkdocs_config(data: dict, path=""):
    """Writes the mkdocs configuration to a file."""
    config_path = path or os.path.join(os.path.dirname(__file__), "mkdocs.yml")
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True)
    except Exception as e:
        logging.error(f"Error writing configuration file: {e}")
        raise

def gen_weekly_content(years: int):
    """Generates a yearly summary of weekly content."""
    root_path = os.path.dirname(__file__)
    target_path = os.path.join(root_path, f"docs/{years}")
    
    try:
        with open(f"./{years}_weekly_all.md", "w", encoding="utf-8") as pf:
            file_list = [os.path.join(target_path, file) for file in os.listdir(target_path) if file.endswith(".md")]
            for each in sorted(file_list):
                with open(each, "r", encoding="utf-8") as f:
                    pf.write(f"This is the weekly newsletter for {years} year\n\n" + f.read() + "\n\n")
    except Exception as e:
        logging.error(f"Error generating weekly content: {e}")
        raise

def gen_weekly_title(years: int):
    """Generates titles for weekly newsletters."""
    root_path = os.path.dirname(__file__)
    target_path = os.path.join(root_path, f"docs/{years}")
    res_dict = {}
    
    try:
        for file in os.listdir(target_path):
            if file.endswith(".md") and "Weekly Newsletter" in file:
                match_obj = re.search(r"Episode (.*?)", file)
                if match_obj:
                    res_dict[match_obj[1]] = file
        
        res_list = []
        for i in sorted(res_dict):
            file_name = res_dict[i]
            date_cycle = file_name.split(".")[0]
            logging.info(f"- Episode {i} ({date_cycle}): ./{years}/{file_name}")
            res_list.append({f"Episode {i} ({date_cycle})": f"./{years}/{file_name}"})

        mkdocs_config = read_mkdocs_config()
        for each in mkdocs_config["nav"]:
            for key in each.keys():
                if str(years) in key:
                    each[key] = res_list[::-1]  # Reverse order
        write_mkdocs_config(mkdocs_config)
    except Exception as e:
        logging.error(f"Error generating weekly titles: {e}")
        raise

if __name__ == "__main__":
    try:
        # Generate annual weekly content summary
        gen_weekly_content(2023)
        # Generate sitemap
        gen_sitemap()
        # Persist weekly content to the database
        parse_md()
        # Generate RSS feed
        gen_rss()
        # Generate titles for the latest weekly
        gen_weekly_title(2024)
    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
