import os
import json
import click

from .apng import APNGProcessorHeadless
from .version import __version__


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        # Show the UI
        click.echo(f"Running apngc {__version__} with UI...")
        from .ui import start
        start()
    else:
        click.echo(f"Running apngc {__version__} {ctx.invoked_subcommand}...")


@cli.command()
@click.option("--settings",
              help="Specify settings preset JSON filename or full path")
@click.option("--folder",
              help="Specify the folder containing the source "
                   "sequence to convert")
@click.option("--output_path", help="The output directory", default=None)
@click.option("--tinify",
              help="Override tinify API key (instead of using"
                   " from settings file)",
              default=None)
def headless(settings, folder, output_path, tinify):
    click.echo('Processing headless')

    folder = os.path.abspath(folder)

    with open(settings, "r") as f:
        settings = json.load(f)

    # Override tinify API
    if tinify:
        settings["tinify_key"] = tinify

    # Override output path
    if output_path:
        settings["output_path"] = output_path

    print("Found settings:")
    print(json.dumps(settings, indent=4))

    processor = APNGProcessorHeadless(folder, settings)
    processor.process()


def main():
    cli()


if __name__ == "__main__":
    main()
