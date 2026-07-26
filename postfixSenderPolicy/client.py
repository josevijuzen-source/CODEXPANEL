#!/usr/local/CodexCP/bin/python
import socket
import sys
sys.path.append('/usr/local/CodexCP')
from plogical.CodexCPLogFileWriter import CodexCPLogFileWriter as logging
import argparse
from plogical.mailUtilities import mailUtilities

class cacheClient:
    cleaningPath = '/home/codexpanel/purgeCache'

    @staticmethod
    def handleCachePurgeRequest(command):
        try:
            mailUtilities.checkHome()
            writeToFile = open(cacheClient.cleaningPath, 'w')
            writeToFile.write(command)
            writeToFile.close()

        except BaseException as msg:
            logging.writeToFile(str(msg) + ' [cacheClient.handleCachePurgeRequest]')


def main():

    parser = argparse.ArgumentParser(description='CodexPanel Email Policy Cache Cleaner')
    parser.add_argument('function', help='Specific a function to call!')


    args = parser.parse_args()

    if args.function == "hourlyCleanup":
        command = 'CodexPanelCleaner hourlyCleanup'
        cacheClient.handleCachePurgeRequest(command)
    elif args.function == 'monthlyCleanup':
        command = 'CodexPanelCleaner monthlyCleanup'
        cacheClient.handleCachePurgeRequest(command)


if __name__ == "__main__":
    main()