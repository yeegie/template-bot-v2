from app.infrastructure.bootstrap import init_app
import asyncio


def main():
    asyncio.run(init_app())

    from app.cli import register_commands
    cli = register_commands()
    cli()

if __name__ == "__main__":
    main()
