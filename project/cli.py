"""
project
 
Usage:
  project init
  project -h | --help
  project -v |--version
 
Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
 
Examples:
  project init
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/issamouu69/project-cli
"""
 
 
from inspect import getmembers, isclass
from docopt import docopt
from project import __version__

 
def main():
    """Main CLI entrypoint."""
    import project.commands as commands #all our supported commands
    options = docopt(__doc__, version=__version__)
    #see if command is present
    for k, v in options.items():
      if v and hasattr(commands, k): # v is true for the called command
          module = getattr(commands, k)
          commands = getmembers(module, isclass)
          command = [command[1] for command in commands if command[0] != 'Base'][0]
          command = command(options)
          command.run()