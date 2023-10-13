from source.parser import is_name, parse_name
from source.myfaker import print_fake_name
from source.logger import write_log


def main() -> None:
    if is_name():
        parse_name()
        print_fake_name()
    else:
        print("Tell me Your name, please. (Run cmd [--help] for help)")
        msg = "Failed"
        # write_log(msg)


if __name__ == "__main__":
    main()
