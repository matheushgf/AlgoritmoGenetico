from enum import Enum
from colorama import Fore, Back, Style

class ClasseLog(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = Fore.BLACK + Back.YELLOW + Style.DIM
    FAIL = Fore.BLACK + Back.RED + Style.DIM
    ENDC = Style.RESET_ALL
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = Fore.BLACK + Back.GREEN + Style.DIM
