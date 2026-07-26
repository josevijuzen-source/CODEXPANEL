import subprocess, shlex
import install
import installLog as logging
import time

class mysqlUtilities:

    @staticmethod
    def createDatabase(dbname, dbuser, dbpassword, publicip):

        try:
            createDB = "CREATE DATABASE IF NOT EXISTS " + dbname

            try:
                from json import loads
                mysqlData = loads(open("/etc/codexpanel/mysqlPassword", 'r').read())

                initCommand = 'mariadb -h %s --port %s -u %s -p%s -e "' % (mysqlData['mysqlhost'], mysqlData['mysqlport'], mysqlData['mysqluser'], mysqlData['mysqlpassword'])
                remote = 1
            except:
                passFile = "/etc/codexpanel/mysqlPassword"

                f = open(passFile)
                data = f.read()
                password = data.split('\n', 1)[0]

                initCommand = 'mariadb -u root -p' + password + ' -e "'
                remote = 0

            command = initCommand + createDB + '"'

            if install.preFlightsChecks.debug:
                print(command)
                time.sleep(10)

            cmd = shlex.split(command)
            res = subprocess.call(cmd)

            if res == 1:
                logging.InstallLog.writeToFile("[WARN] CREATE DATABASE %s failed (may already exist)" % dbname)

            if remote:
                createUser = "CREATE USER IF NOT EXISTS '" + dbuser + "'@'%s' IDENTIFIED BY '" % (publicip) + dbpassword + "'"
            else:
                createUser = "CREATE USER IF NOT EXISTS '" + dbuser + "'@'localhost' IDENTIFIED BY '" + dbpassword + "'"

            command = initCommand + createUser + '"'

            if install.preFlightsChecks.debug:
                print(command)
                time.sleep(10)

            cmd = shlex.split(command)
            res = subprocess.call(cmd)

            if res == 1:
                logging.InstallLog.writeToFile("[WARN] CREATE USER %s failed (may already exist)" % dbuser)
            else:

                if remote:

                    ### DO Check

                    if mysqlData['mysqlhost'].find('ondigitalocean') > -1:

                        alterUserPassword = "ALTER USER 'codexpanel'@'%s' IDENTIFIED WITH mysql_native_password BY '%s'" % (
                        publicip, dbpassword)
                        command = initCommand + alterUserPassword + '"'

                        if install.preFlightsChecks.debug:
                            print(command)
                            time.sleep(10)

                        cmd = shlex.split(command)
                        subprocess.call(cmd)

                    ## RDS Check

                    if mysqlData['mysqlhost'].find('rds.amazon') == -1:
                        dropDB = "GRANT ALL PRIVILEGES ON " + dbname + ".* TO '" + dbuser + "'@'%s'" % (publicip)
                    else:
                        dropDB = "GRANT INDEX, DROP, UPDATE, ALTER, CREATE, SELECT, INSERT, DELETE ON " + dbname + ".* TO '" + dbuser + "'@'%s'" % (publicip)
                else:
                    dropDB = "GRANT ALL PRIVILEGES ON " + dbname + ".* TO '" + dbuser + "'@'localhost'"

                command = initCommand + dropDB + '"'

                if install.preFlightsChecks.debug:
                    print(command)
                    time.sleep(10)

                cmd = shlex.split(command)
                res = subprocess.call(cmd)

                if res == 1:
                    return 0

            return 1
        except BaseException as msg:
            return 0