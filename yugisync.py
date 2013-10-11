"""
Usage:
"""
__author__ = 'Emanuil Tolev'


def export():
    # Copy the whole Common dir to the backup git repo
    # copy yugi, kaiba and joey deck to backup repo
    # export registry keys (be mindful of 64 vs 32 bit systems) to
    #   backup repo
    pass


def restore():
    backup_local()
    # delete current Common dir
    # restore Common dir from backup repo
    # restore decks from backup repo
    # import registry keys
    pass


def push():
    pass


def pull():
    pass


def backup_local():
    # copy current Common dir to "OLD "
    # copy yugi,kaiba,joey decks to .old
    pass