from dotbot import Plugin

class ZypperPlugin(Plugin):
    def __init__(self, packages, repositories=[]):
        super().__init__()
        self.packages = packages
        self.repositories = repositories

    def can_handle(self, directive):
        return directive in ['zypper']

    def handle(self, directive, data):
        if directive != 'zypper':
            raise ValueError(f"Unsupported directive: {directive}")

        command = ['zypper', '--non-interactive']

        for repo in self.repositories:
            command += ['--repo', repo]

        command += ['install'] + self.packages

        return self._execute(command)

    def _execute(self, command):
        return self._log_execute(command)

    def _log_execute(self, command):
        self._log.debug(f"Executing: {' '.join(command)}")
        return self._create_subprocess(command).wait()

    def _create_subprocess(self, command):
        return self._process_runner.run(command)
