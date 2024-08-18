import json
# import yaml
import logging

from pathlib import Path
from ruamel.yaml import YAML

logger = logging.getLogger(__name__)

def load_config(path):
    logger.debug(f'Загрузка конфигурации сервиса по пути {path}')
    yaml = YAML()
    with open(path, 'r') as file:
        logger.debug(f'Загрузка конфигурации выполнена успешно')
        return yaml.load(file)


def load_schema(profile_path: str, version: str) -> map:
    logger.debug(f'Загрузка профайла')
    data_folder = Path("{current_dir}/profiles/{profile}".format(
        current_dir=Path(__file__).parent.resolve(), profile=profile_path))
    file_to_open = data_folder / "schema.json" 
    if not file_to_open.exists():
        raise FileNotFoundError('Не найден нужный профайл')

    logger.debug(f'Профайл найден, загружаем правила')    
    with open(file_to_open, 'r') as file:
        schema = json.load(file)
    return schema


# def load_rules(profile, version):
#     rules_path = f'profiles/{profile}/{version}/rules.yaml'
#     with open(rules_path, 'r') as file:
#         return yaml.safe_load(file)['rules']
