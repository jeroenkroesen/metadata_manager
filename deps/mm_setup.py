from pathlib import Path
from rich import print, inspect


def setup_manager(
    root: str = '../metadata',
    repo: str = '../metadata/metadata',
    data: str = '../metadata/metadata',
    stash: str = '../metadata/stash',
    create: bool = False
) -> bool:
    # Load paths
    root = Path(root).resolve()
    repo = Path(repo).resolve()
    data = Path(data).resolve()
    stash = Path(stash).resolve()
    # Set initial state
    valid = True
    # Validate path existence
    ## Root folder
    print('[bold]Checking Root[/bold]')
    print(f'Folder: [bright_white]{str(root)}[/bright_white]')
    if root.exists():
        print(f'[bright_green]Root [bold]exists[/bold][/bright_green]')
    else:
        valid = False
        print(f'[bright_red]WARNING! Root [bold]does not exist[/bold][/bright_red]')
    print()
    ## Repo folder
    print('[bold]Checking Repo[/bold]')
    print(f'Folder: [bright_white]{str(repo)}[/bright_white]')
    if repo.exists():
        print(f'[bright_green]Repo [bold]exists[/bold][/bright_green]')
    else:
        valid = False
        print(f'[bright_red]WARNING! Repo [bold]does not exist[/bold][/bright_red]')
    print()
    ## Data folder
    print('[bold]Checking Data folder[/bold]')
    print(f'Folder: [bright_white]{str(repo)}[/bright_white]')
    if data.exists():
        print(f'[bright_green]Data [bold]exists[/bold][/bright_green]')
    else:
        valid = False
        print(f'[bright_red]WARNING! Data [bold]does not exist[/bold][/bright_red]')
    print()
    ## Stash folder
    print('[bold]Checking Stash[/bold]')
    print(f'Folder: [bright_white]{str(stash)}[/bright_white]')
    if stash.exists():
        print(f'[bright_green]Stash [bold]exists[/bold][/bright_green]')
    else:
        valid = False
        print(f'[bright_red]WARNING! Stash [bold]does not exist[/bold][/bright_red]')

    return valid