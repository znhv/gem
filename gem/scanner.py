import jsonschema

from jsonschema.exceptions import ValidationError
from gem.report import generate_report

def validate_with_extended_schema(config_path, config, schema):
    print('\nConfiguration Check Summary:')
    print('──────────────────────────────────')

    validator = jsonschema.Draft7Validator(schema)
    errors = list(validator.iter_errors(config))
    error_summary = {'error': 0, 'warn': 0, 'info': 0}

    if not errors:
        print("✓ All configurations are secure.")
    else:
        for error in errors:
            schema_path = list(error.schema_path)[:-1]
            subschema = extract_subschema(schema, schema_path)

            warning_level = subschema.get("warning_level", "error")
            message = subschema.get("message", error.message)
            recommendation = subschema.get("recommendation", "")

            # Определяем строку, на которой произошла ошибка
            error_line = "unknown"
            if error.absolute_path:
                try:
                    current_element = config
                    for key in list(error.absolute_path)[:-1]:
                        current_element = current_element[key]
                    error_line = current_element.lc.line + 1
                except Exception as exc:
                    print(f"Error determining line number: {exc}")

            # Определяем символ статуса и увеличиваем счетчик
            if warning_level == "error":
                status_symbol = "ERROR:"
                error_summary['error'] += 1
            elif warning_level == "warn":
                status_symbol = "WARN:"
                error_summary['warn'] += 1
            else:
                status_symbol = "INFO:"
                error_summary['info'] += 1

            # Вывод сообщения
            print(f"{status_symbol} {message} (line {error_line})")
            if recommendation:
                print(f"  ➜ {recommendation}", '\n')

    print('──────────────────────────────────')
    total_issues = f"{error_summary['error']} errors, {error_summary['warn']} warnings, {error_summary['info']} infos"
    print(f"Total Issues: {total_issues}")
    print("Fix critical errors to ensure system security and stability.\n")


def extract_subschema(schema, path):
    subschema = schema
    for key in path:
        if isinstance(subschema, dict):
            subschema = subschema.get(key, {})
        elif isinstance(subschema, list):
            try:
                subschema = subschema[int(key)]
            except (ValueError, IndexError):
                subschema = {}
                break
        else:
            subschema = {}
            break
    return subschema
