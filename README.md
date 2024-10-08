# metadata_manager

## Installation

### Clone this repo
```bash
git clone git@github.com:jeroenkroesen/metadata_manager.git
```
***

### Create and activate virtual env
Enter the manager folder
```bash
cd metadata_manager
```
  
Create
```bash
python3 -m venv env
```

Activate  
```bash
source env/bin/activate
```
***

### Install dependencies
External deps
```bash
pip install pydantic pydantic-settings pendulum "rich[jupyter]" jupyterlab pandas "fastapi[all]"
```
  
Internal lib  
```bash
pip install git+ssh://git@github.com/jeroenkroesen/metadata_lib.git@main
```
***

### Create Data Directories
Make sure you're in the metadata_manager folder
```bash
# Root folder
mkdir ../metadata
# stash folder
mkdir ../metadata/stash
# Repo
cd ../metadata
Now clone your metadata repository into a folder here called `metadata`
```
