import sys
import yaml
import argparse as ap


def main():
    parser = ap.ArgumentParser()
    parser.add_argument("venvpath")
    parser.add_argument("config_filename")
    args = parser.parse_args()

    local_venv_loc = args.venvpath

    if sys.platform == 'win32' or sys.platform == 'cygwin':
        local_venv_loc += "\\Scripts"
    else:
        local_venv_loc += '/bin'

    main_script_location = f'cdm8_asm_brd_script.py'

    cfg = {
        "buildStrategy": {
            "strategyClass": "ru.nsu_null.npide.ide.projectstrategies.defaults.delegators.BuilderDelegatorStrategy",
            'extraConfiguration': {
                'executable': local_venv_loc + "/python",
                "script": 'cdm8_asm_brd_script.py'
            }
        },
        'runStrategy': {
            'strategyClass': "ru.nsu_null.npide.ide.projectstrategies.defaults.delegators.RunnerDelegatorStrategy",
            'extraConfiguration': {
                'executable': local_venv_loc + "/python",
                "script": 'cdm8_asm_brd_script.py'
            }
        },
        'debugStrategy': {
            'strategyClass': "ru.nsu_null.npide.ide.projectstrategies.defaults.delegators.DebuggerDelegatorStrategy",
            'extraConfiguration': {
                'executable': local_venv_loc + "/python",
                "script": 'cdm8_asm_brd_script.py',
                "step": "S",
                "continue": "C"
            }
        },
        'grammarConfigs': [
            {
                "sourceFileExtension": 'asm',
                'grammar': 'asm.g4',
                'syntaxHighlighter': 'colors.json'
            }
        ]
    }
    with open(args.config_filename, 'w') as file:
        yaml.dump(cfg, file, default_style='"')
    with open(args.config_filename, 'r') as file:
        print(yaml.load(file, yaml.Loader))


if __name__ == '__main__':
    main()
