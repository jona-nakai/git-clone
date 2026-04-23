import sys
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(
        prog='jit',
        description='a clone of git version control system')

subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

# jit init command
jit_parser = subparsers.add_parser('init', help='Initialize a new repository')
jit_parser.add_argument('path', nargs='?', default= '.')
def cmd_init(args):
    p = Path(args.path)
    dirs = ['.jit/objects', '.jit/refs/heads', '.jit/refs/tags']

    message = f'Reinitialized existing Jit repository in {(p / '.jit').resolve()}'
    
    for dir in dirs:
        p_dir = p / dir
        p_dir.mkdir(parents=True, exist_ok=True)
    
    if (p / '.jit' / 'HEAD').exists():
        print(message)
        return

    message = f'Initialized empty Jit repository in {(p / '.jit').resolve()}'

    with open((p / '.jit' / 'HEAD'), 'w') as f:
        f.write('ref: refs/heads/main')
    
    print(message)

def main(argv=sys.argv[1:]):
    args = parser.parse_args(argv)
    if args.subcommand == None:
        print('Help')
    match args.subcommand:
        case "init"         : cmd_init(args)
        case "hash-object"  : cmd_hash_object(args)
        case "cat-file"     : cmd_cat_file(args)
        case "log"          : cmd_log(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "checkout"     : cmd_checkout(args)
        case "show-ref"     : cmd_show_ref(args)
        case "tag"          : cmd_tag(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "ls-files"     : cmd_ls_files(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "status"       : cmd_status(args)
        case "add"          : cmd_add(args)
        case "rm"           : cmd_rm(args)
        case "commit"       : cmd_commit(args)
        case _              : print("Bad command.")
