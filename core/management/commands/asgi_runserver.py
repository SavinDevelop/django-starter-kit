from django.core.management.base import BaseCommand
import uvicorn

class Command(BaseCommand):
    help = "Run Django using Uvicorn (ASGI)."

    def add_arguments(self, parser):
        parser.add_argument("--host", default="127.0.0.1")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--reload", action="store_true")
        parser.add_argument("--workers", type=int, default=1)

    def handle(self, *args, **options):
        uvicorn.run(
            "core.asgi:application",  # твій asgi.py
            host=options["host"],
            port=options["port"],
            reload=options["reload"],
        )
