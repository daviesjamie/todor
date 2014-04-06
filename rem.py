import argparse
import sys


def _build_parser():
    parser = argparse.ArgumentParser()

    # ACTIONS
    actions = parser.add_argument_group('Actions')

    # Initialise task list
    actions.add_argument('--init', dest='init')

    # Edit a task
    actions.add_argument('-e', '--edit', dest='edit', metavar='TASK HASH')

    # Complete a task
    actions.add_argument('-c', '--complete', dest='complete', metavar='TASK HASH')

    # Delete a task
    actions.add_argument('-rm', '--remove', dest='remove', metavar='TASK HASH')


    # OUTPUT OPTIONS
    output = parser.add_argument_group('Output Options')

    # Grep for a task
    output.add_argument('-g', '--grep', dest='grep', metavar='SEARCH TERM(S)')

    # Detailed task listing
    output.add_argument('-l', '--long', dest='detailed', action='store_true')

    # Simple task listing
    output.add_argument('-s', '--simple', dest='simple', action='store_true')

    # List completed tasks
    output.add_argument('--completed', dest='completed', action='store_true')


    return parser


def _main():
    args, text = _build_parser().parse_known_args()
    print args
    print text


if __name__ == '__main__':
    _main()