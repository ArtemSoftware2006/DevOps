import os

def find_rc(rc_name='.examplerc'):
    var_name = 'EXAMPLERC_DIR'
    if var_name in os.environ:
        var_path = os.path.join(f'${var_name},', rc_name)
        config_path = os.path.expandvars(var_path)
        print(f'Check {config_path}')
        check_config_path(config_path)
    
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f'Check {config_path}')
    check_config_path(config_path)

    home_dir = '~/'
    config_path = os.path.join(home_dir, rc_name)
    print(f'Check {config_path}')
    check_config_path(config_path)

    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f'Check {config_path}')
    check_config_path(config_path)

    print(f'Config file {rc_name} has not been found')
def check_config_path(config_path):
    if os.path.exists(config_path):
        print(f'Config file {config_path} has been found')
        exit(0)
    
find_rc()
