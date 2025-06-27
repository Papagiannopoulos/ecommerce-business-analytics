
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_name: str, download_path: str ='.') -> None:
    """
    Download a dataset from Kaggle.

    Parameters:
    - dataset_name: str, dataset identifier in the form 'username/dataset-name'
    - download_path: str, local directory to save the dataset
    """
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Dataset '{dataset_name}' downloaded and extracted to '{download_path}'")