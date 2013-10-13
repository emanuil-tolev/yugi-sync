"""
Usage: python yugisync.py pull|push
Backs up everything needed to restore your current game options,
deck and card list to a git repository. If the repository is uploaded
to a service like GitHub.com, this will also upload the changes there.

Example: python yugisync.py push on your own laptop and then python
yugisync.py pull on a friend's laptop will give you your card list,
decks, replays and game options to play with. Yugi-sync is always
careful, so it will never overwrite your friend's data. Obviously in
this case you and your friend can't have different decks and options.
Yugi-sync allows you both to play with and contribute to the same
deck.
"""

# later...
'''Watches all important files for changes and backs everything needed
to restore your deck whenever the game files change (e.g. you export
a deck, you win cards, you change the game options).'''
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
    # git push the backup repo
    pass


def pull():
    # git pull the backup repo
    pass


def backup_local():
    # copy current Common dir to "OLD "
    # copy yugi,kaiba,joey decks to .old
    pass