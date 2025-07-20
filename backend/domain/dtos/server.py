from dataclasses import dataclass


@dataclass
class ServerCreateDTO:
    name: str
    ip: str
    port: int
    account: str
    pkey: str
