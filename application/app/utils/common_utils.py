import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPENAPI_PATH = os.path.join(BASE_DIR, 'docs', 'openapi.yaml')

def load_openapi_spec(file_path:str):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"OpenAPI specification not found at {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing OpenAPI specification: {e}")
        return None
    
openapi_spec = load_openapi_spec(OPENAPI_PATH)