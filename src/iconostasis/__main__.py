import click
from iconostasis import Iconostasis
# from . import __version__

@click.command()
@click.option('--files', '-f', multiple=True)
# @click.version_option(version=__version__)
def main(files) -> None:
    Iconostasis(*files)


if __name__ == "__main__":
    main(prog_name="iconostasis")  # pragma: no cover
