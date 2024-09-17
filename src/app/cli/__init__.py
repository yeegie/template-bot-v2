from .database.database import database_group
import click


def register_commands() -> click.Group:
    return click.Group(
        commands={
            "database": database_group,
        }
    )
