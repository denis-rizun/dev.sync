from io import StringIO

import paramiko
from paramiko import SSHException, AuthenticationException

from backend.core.logger import Logger
from backend.domain.abstractions.services.ssh import ISSHService

logger = Logger.setup_logger(__name__)


class SSHService(ISSHService):
    def __init__(self, ip: str, username: str, password_or_key: str, port: int = 22) -> None:
        self.ip = ip
        self.port = port
        self.username = username
        self.password_or_key = password_or_key
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def execute(self, script: str, timeout: int = 300) -> tuple[bool, str]:
        self.connect()
        success, result = self.run_commands(shell_script=script, timeout=timeout)
        self.close()
        return success, result

    def connect(self) -> None:
        try:
            pkey_file = StringIO(self.password_or_key.strip() + '\n')
            private_key = paramiko.RSAKey.from_private_key(pkey_file)
            self.client.connect(
                hostname=self.ip,
                port=self.port,
                username=self.username,
                pkey=private_key,
                timeout=5
            )
            logger.info("[SSHService]: Connected to server")
        except (SSHException, AuthenticationException, ValueError) as e:
            logger.warning(f"[SSHService]: Error while connecting to server: {e}")
            self.client.connect(
                hostname=self.ip,
                port=self.port,
                username=self.username,
                password=self.password_or_key,
                timeout=5
            )
            logger.info("[SSHService]: Connected to server")

    def run_commands(self, shell_script: str, timeout: int = 300) -> tuple[bool, str]:
        commands = shell_script.split('\n')
        commands = [cmd.strip() for cmd in commands if cmd.strip()]
        command_string = ' && '.join(commands)

        stdin, stdout, stderr = self.client.exec_command(command_string, timeout=timeout)
        output = stdout.read().decode()
        error = stderr.read().decode()

        logger.info("[SSHService]: Command executed")

        if not output and error:
            return False, error

        return True, output

    def close(self) -> None:
        self.client.close()
        logger.info("[SSHService]: Connection closed")
