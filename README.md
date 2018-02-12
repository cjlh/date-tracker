# date-tracker

A Python script for keeping track of important dates.

[Further description to be written]


## Getting started


### Dependencies

This script requires Python 3 and the [PyYAML](https://pypi.python.org/pypi/PyYAML) module (this may be included by default with your Python 3 installation).


### Installation

1. Save `dates.py` and `events.example.yaml` to a location of your choice (this is where you will run the script from):

    ```
    $ git clone https://github.com/cjlh/date-tracker.git /path/to/desired/directory
    ```

   *Or:*

    ```
    $ wget https://raw.githubusercontent.com/cjlh/date-tracker/master/dates.py
    $ wget https://raw.githubusercontent.com/cjlh/date-tracker/master/events.example.yaml
    ```

2. Rename `events.example.yaml` to `events.yaml` and add your own event details (see ['Use' section](#Use) for more details).

3. *(Optional)* Set an alias in your shell for quick use. Examples:

   bash (\~/.bashrc) and zsh (\~/.zshrc):

    ```
    alias dates="python3 /path/to/dates.py"
    ```

   fish (\~/.config/fish/config.fish):

    ```
    alias dates "python3 /path/to/dates.py"
    ```


## Use

[Instructions to be written]


## TODO

- [ ] Add screenshot
- [ ] Write usage instructions
- [x] Add support for YAML events file
- [ ] * Add support for categories (with the ability to view only one list using command line args)
- [ ] Append date to day - i.e. "(Thursday)" -> "(Thursday 10th March)"
- [ ] Rename example `events.yaml` to `example_events.yaml` and add support for multiple events files
- [ ] Automatically create `events.yaml` on first run and do not require its existence to run
- [ ] Enable adding events via the program
- [ ] Write help text
- [ ] Comprehensively comment code
- [ ] Add option to sort events chronologically


## License

This project is licensed under the GNU GPLv3 License.

***
[https://github.com/cjlh/date-tracker](https://github.com/cjlh/date-tracker)
