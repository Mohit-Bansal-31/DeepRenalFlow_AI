import os
from box.exceptions import BoxValueError
import yaml
from DeepRenalFlow import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file path and returns ConfigBox object

    Args:
        path_to_yaml (Path): Path to the YAML file
        
    Raises:
        ValueError: if yaml file is empty or cannot be read
        e: empty file

    Returns:
        ConfigBox: A ConfigBox object containing the YAML data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} : Loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        logger.error(f"Error reading yaml file {path_to_yaml}: {e}")
        raise e
    
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): List of path of directories
        verbose (bool, optional): Used to select whether we want logs or not. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves Json data to a file

    Args:
        path (Path): Path to json file
        data (dict): Data to be saved in file
    """
    with open(path, "w") as f:
        json.dump(data,f,indent=4)
        
    logger.info(f"Json file saved at: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads Json file data to ConfigBox object

    Args:
        path (Path): Path to json file

    Returns:
        ConfigBox: ConfigBox object containing the data from the json file
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"Json file loaded successfully from: {path}")
    return ConfigBox(content)



@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save Binary data to a file

    Args:
        data (Any): Data to be saved in file
        path (Path): Path to file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at: {path}")
    
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load Binary data from a file

    Args:
        path (Path): Path to Binary file

    Returns:
        Any: Data loaded from the binary file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of file in Kilobytes (KB)

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    logger.info(f"Size of the file {path} is: {size_in_kb} KB")
    return f"~ {size_in_kb} KB"


@ensure_annotations
def decodeImage(imgstring: str,fileName: Path):
    """Decode a encoded image string and save it to a file.

    Args:
        imgstring (str): Encoded image string.
        fileName (Path): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    
    with open(fileName, 'wb') as f:
        logger.info(f"Decoding image and saving to: {fileName}")
        f.write(imgdata)

        
        
        
@ensure_annotations
def encodeImageIntoBase64(croppedImagePath:Path):
    """Encode an image file into a base64 string.

    Args:
        croppedImagePath (Path): Path to the image file to be encoded.

    """
    with open(croppedImagePath, "rb") as f:
        logger.info(f"Encoding image: {croppedImagePath} into base64")
        return base64.b64encode(f.read())
