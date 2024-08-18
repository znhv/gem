import sys
import click
import logging

from gem.loader import load_config, load_schema
from gem.scanner import validate_with_extended_schema
from gem.report import generate_report

logger = logging.getLogger(__name__)

@click.command()
@click.option('--config', required=True, help='Path to configuration file')
@click.option('--profile', required=True, help='Profile name (e.g., prometheus)')
@click.option('--version', required=False, help='Profile version (e.g., 2.0)')
def cli(config, profile, version):
    cfg = load_config(config)
    scheme = load_schema(profile, version)
    validate_with_extended_schema(config, cfg, scheme)
    # rules = load_rules(config)
    # results = scan(config)
    
    # results = scan(config, rules)
    # generate_report(results)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    cli()
