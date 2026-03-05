# ATOC 4815/5815 Git Practice Repository

Welcome! This repository is a space to practice Git commands. If something goes wrong, just delete the folder and clone again.

## Quick Setup

```bash
# fork this repo first!! 

# Clone this repository
git clone https://github.com/UserName/atoc4815-git.git

# Move into the folder
cd atoc4815-git
```

## Exercises

### Exercise 1: Boulder Temperatures (`boulder_temperatures.py`)
- Add your name to the file
- Calculate average, max, and min January temperatures
- Commit your changes

### Exercise 2: Denver Wind Analysis (`denver_wind_analysis.py`)
- Calculate average wind speed
- Count wind advisory days (winds > 25 mph)
- Commit your changes

## The 5-Command Cheat Sheet

| Command | What it does | Safe? |
|---------|-------------|-------|
| `git status` | Shows what changed | 100% safe |
| `git add <file>` | Stages a file for saving | Safe |
| `git commit -m "message"` | Saves a snapshot | Safe |
| `git push` | Uploads to GitHub | Safe |
| `git pull` | Downloads from GitHub | Safe |

## The Daily Workflow

```bash
git status                        # 1. What changed?
git add myfile.py                 # 2. Stage changes
git commit -m "Describe changes"  # 3. Save snapshot
git push                          # 4. Upload to GitHub
```

## Something went wrong?

The nuclear option always works:

```bash
cd ..
rm -rf atoc4815_git
git clone https://github.com/WillyChap/atoc4815_git.git
```

This deletes your local copy and starts fresh. Your work on GitHub is safe.

## Contact
edited by Will

- Will Chapman (wchapman@colorado.edu)
- Office hours: Tu 11:15-12:15p, Th 9-10a (Aerospace Cafe)


Edited on GitHub by Matthew
