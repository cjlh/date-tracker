# date-tracker

A Python script for keeping track of important dates.

[Further description to be written]


## Getting started


### Dependencies

This script requires Python 3.


### Installation

1. Save `dates.py` and `events.yaml` to a location of your choice (this is where you will run the script from):

    ```
    $ git clone https://github.com/cjlh/date-tracker.git /path/to/desired/directory
    ```

   *Or:*

    ```
    $ wget https://raw.githubusercontent.com/cjlh/date-tracker/master/dates.py
    $ wget https://raw.githubusercontent.com/cjlh/date-tracker/master/events.yaml
    ```

2. *(Optional)* Set an alias in your shell for quick use. Examples:

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

- [ ] Write usage instructions
- [x] Add support for YAML events file
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
