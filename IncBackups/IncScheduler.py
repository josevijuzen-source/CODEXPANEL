import argparse
import sys
sys.path.append('/usr/local/CodexCP')
from plogical.processUtilities import ProcessUtilities

def main():

    parser = argparse.ArgumentParser(description='CodexPanel Installer')
    parser.add_argument('function', help='Specific a function to call!')
    args = parser.parse_args()

    command = f"/usr/local/CodexCP/bin/python /usr/local/CodexCP/plogical/IncScheduler.py '{args.function}'"
    ProcessUtilities.normalExecutioner(command)


if __name__ == "__main__":
    main()