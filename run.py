import asyncio
from app import main
from source.logger import write_log

if __name__ == "__main__":
    write_log("New run")

    asyncio.run(main())
