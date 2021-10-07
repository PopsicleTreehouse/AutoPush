#!/usr/bin/env python3
from git import Repo
from os import getcwd

def get_files(commit, change_type):
    return [x.b_path for x in commit if x.change_type == change_type]

def get_msg(commit, change_type, msg):
    files = get_files(commit, change_type)
    return '' if files == [] else f"{msg}: {', '.join(files)}" 

def main(): 
    repo = Repo(getcwd())
    repo.git.add('.')
    unstaged_commit = repo.head.commit.diff()
    msgs = [
        get_msg(unstaged_commit, 'A', "Added"),
        get_msg(unstaged_commit, 'M', "Updated"),
        get_msg(unstaged_commit, 'D', "Removed"),
        get_msg(unstaged_commit, 'R', "Renamed")
    ]
    commit_msg = ', '.join([x for x in msgs if x])
    repo.git.commit('-m', commit_msg)
    repo.git.push('origin', 'master')

if(__name__ == '__main__'):
    main()