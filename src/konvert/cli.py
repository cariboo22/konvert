import typer

from .module import konverting

app = typer.Typer()
app.command()(konverting)

if __name__ == "__main__":
    app()
