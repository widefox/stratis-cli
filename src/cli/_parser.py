import argparse

from ._logical import build_logical_parser
from ._physical import build_physical_parser


def build_list_parser(parser):
    """
    Generate the parser appropriate for displaying information.

    :param ArgumentParser parser: a parser
    :returns: a completed parser for listing pools
    :rtype: ArgumentParser
    """
    return parser


def build_create_parser(parser):
    """
    Generates the parser appropriate for creating a pool.

    :param ArgumentParser parser: a parser
    :returns: a completed parser for creating a pool
    :rtype: ArgumentParser
    """
    parser.add_argument(
       'name',
       action='store',
       help='name to assign to pool'
    )
    parser.add_argument(
       'device',
       help='make device D a member of this pool',
       metavar='D',
       nargs='+'
    )
    parser.add_argument(
       '--force',
       action="store_true",
       default=False,
       help="overwrite all existing data and metadata on selected devices"
    )
    parser.add_argument(
       '--redundancy',
       action='store',
       choices=['single'],
       default='single',
       help="redundancy selection for this pool"
    )
    return parser


def gen_parser():
    """
    Make the parser.

    :returns: a fully constructed parser for command-line arguments
    :rtype: ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Stratis Storage Manager")

    subparsers = \
       parser.add_subparsers(dest='subparser_name', title='subcommands')

    subparser_names = ('cache', 'create', 'dev', 'list', 'vol')

    subparser_table = dict()

    subparser_table['create'] = \
       subparsers.add_parser('create', description="Create New Stratis Pool")
    build_create_parser(subparser_table['create'])

    subparser_table['list'] = \
       subparsers.add_parser('list', description="List Stratis Pools")
    build_list_parser(subparser_table['list'])

    subparser_table['logical'] = \
       subparsers.add_parser(
          'logical',
          description="Administer Logical Aspects of Specified Pool"
       )
    build_logical_parser(subparser_table['logical'])

    subparser_table['physical'] = \
       subparsers.add_parser(
          'physical',
          description="Administer Physical Aspects of Specified Pool"
       )
    build_physical_parser(subparser_table['physical'])


    return parser