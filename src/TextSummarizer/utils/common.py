import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from src.TextSummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Read yaml file and return its content as ConfigBox object
    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(path_to_yaml)
            logger.info(f"yaml file: {path_to_yaml} successfully loaded")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def creat_directories(path_to_directories: list, verbose=True):
    '''
    Create directories given a list of path
    '''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    '''
    Get the size in KB
    '''
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"