__all__ = ["database_group"]

import click
from app.cli.database.command import DatabaseCommands
from app.utils.ioc import ioc
from app.infrastructure.config import RootConfig, MysqlDatabase


config = ioc.get(RootConfig)
database_commands = DatabaseCommands(config.databases)


# Commands
create_db_command = click.Command(
    name="create_db",
    callback=database_commands.create_db,
)


# Command group
database_group = click.Group(
    commands={
        "create_db": create_db_command,
    }
)
