from subprocess import Popen, PIPE


class Ping(object):
    hostname = ''
    status_code = 0
    is_online = False
    has_checked = False

    def __init__(self, hostname):
        self.hostname = hostname

    def run_ping(self):
        if self.has_checked:
            return

        ping_response = Popen("ping -c 1 " + self.hostname, stdout=PIPE, stderr=PIPE, shell=True)
        ping_response.wait()

        self.status_code = ping_response.returncode

        if self.status_code == 0:
            self.is_online = True
        else:
            self.is_online = False
        self.has_checked = True

        return self
