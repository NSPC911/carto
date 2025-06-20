## carto

> Your map through the uncharted directories

> [!caution]
> This project is in its very early stages. Feedback is appreciated, but this cannot be daily-driven yet.

### Setup
```py
git clone https://github.com/NSPC911/carto
cd carto
uv sync
```
### Run
```py
uv run src/main.py
```

### Roadmap
This is a list of features that I plan to add before releasing the appropriate version and where they are inspired from.
#### v1
- [x] Directory Autocompletion (explorer)
- [x] Button Navigation (explorer)
- [ ] Keyboard Navigation
  - [x] Directory Navigation (explorer)
  - [ ] Others (superfile)
     - There currently is a bug during my refactoring where due to Action Bar Buttons being seperate classes and their keys are in it, Textual doesn't seem to pass the key event to it. Looking into it.
- [x] Double Click to enter into directories (explorer)
- Configuration (superfile)
  - [x] Base
  - [ ] Schema
  - [x] Extending custom themes via configuration
- [x] [zoxide](https://github.com/ajeetdsouza/zoxide) support (ranger)<br><sub>There is no command line for carto, which means it will use keybinds to launch either a modified current folder bar or a panel</sub>
- [x] Previewing image files using [textual-image](https://github.com/lnqs/textual-image) (superfile)<br><sub>Explorer does support image viewing, but this is a TUI, so inspiration is from superfile</sub>
- [x] Previewing directories (superfile)
- [x] Pinned folder sidebar (superfile)<br><sub>explorer does support pinned sidebar, but it also includes the massive file tree, which I won't add.</sub>
- [ ] Search Bar (superfile)
- [ ] Metadata
- [ ] Clipboard (superfile)
  - [x] Copy files and folders
  - [x] Cut files and folders
  - [ ] Paste files and folders
    - [ ] Warn when overwriting same named files
- [ ] Multiple File Lists
  - [ ] Tabs
  - [ ] VSplit and HSplit
- [ ] Active and Completed processes (superfile)
- [ ] Actions bar (explorer)
  - [ ] Change sort order of files
  - [x] Copy files
  - [x] Cut files
  - [ ] Paste files
  - [x] Create new files/folders
  - [x] Delete files/folders
  - [x] Rename **a** file/folder
- [ ] bat as previewer (using `--force-colorization`)

#### v2
- [ ] Plugins using [pytest-dev/pluggy](https://github.com/pytest-dev/pluggy) or a custom way (i wish not)
- [ ] Cross process clipboard sync (two carto instances should have synced clipboards)
- [ ] Recycle Bin of 1 day when files get overwritten (Currently handled with `sendtotrash` but it doesn't work at times, so not a reliable solution)
