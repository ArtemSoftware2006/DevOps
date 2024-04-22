import os
import pathlib

def find_rc(rc_name = '.examplerc'):
    env_name = "EXAMPLERC_DIR"
    dir_path = os.environ.get(env_name)
    if dir_path:
        dir_path = pathlib.Path(dir_path)
        check_config_path(dir_path / rc_name)

    check_config_path(pathlib.Path.cwd() / rc_name)
    check_config_path(pathlib.Path.home() / rc_name)
    check_config_path(pathlib.Path(__file__).parent / rc_name)

    print(f'Config file {rc_name} has not been found')

def check_config_path(config_path):
    print(f'Check {config_path}')
    if config_path.exists():
        print(f'Config file {config_path} has been found')
        exit(0)

find_rc()