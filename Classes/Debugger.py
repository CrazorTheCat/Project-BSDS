class Debugger:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def error(message):
        print(f"{Debugger.FAIL}[ERROR]{Debugger.ENDC} {message}")

    @staticmethod
    def warning(message):
        print(f"{Debugger.WARNING}[WARNING]{Debugger.ENDC} {message}")

    @staticmethod
    def info(message):
        print(f"[INFO] {message}")