### APNGC

Quickly create tiny compressed animated APNG that look great using reusable preset profiles.

It's using the following under the hood:
- [FFMPEG](https://www.ffmpeg.org/) for resizing image sequences
- [APNG Assembler](https://apngasm.sourceforge.net/) for assembling the APNGs from the PNG sequences
- [tinyPNG API](https://tinypng.com/developers) for compressing them

### Building `apngc` executable

1. Add `ffmpeg` and `apngasm` binaries to the project, like:

_windows_
```
{root}/bin/win/ffmpeg/ffmpeg.exe
{root}/bin/win/apngasm/apngasm64.exe
```

_mac_
```
{root}/bin/mac/ffmpeg/ffmpeg
{root}/bin/mac/apngasm/apngasm
```

2. Run `uv run pyinstaller cli.spec` to build the executable.

_Alternatively you can run it within your own `venv` with the right dependencies as defined in the `pyproject.toml`_