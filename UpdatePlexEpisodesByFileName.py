import re
from plexapi.server import PlexServer
import secrets
baseurl = secrets.baseurl
token = secrets.token
plex = PlexServer(baseurl,token)

# Shownames you want this script to look at. 
shownames = ['Math-U-See', 'Structure and Style for Students', 'NHL Hockey', 'Introduction to Church History']
dryrun = True
verbose = False

for showname in shownames:
    total = 0
    updated = 0
    updaterequired = 0
    updatenotrequired = 0
    print('Examining ' + showname + '...')
    episodes = plex.library.section('TV Shows').get(showname).episodes()
    for episode in episodes:
        total += 1
        newtitle = episode.locations[0]

        # Standard Naming
        newtitle = re.sub('.*?/' + showname + '(?: \(\d{4}\))? - s\d{2,4}e\d{2,4}(?:-e\d{2,4})? - ([^/]+?)\.\w+$', '\g<1>', newtitle, flags=re.IGNORECASE)

        # Date 1
        newtitle = re.sub('.*?/' + showname + '(?: \(\d{4}\))? - \d{4}-\d{2}-\d{2}(?: \d{2} \d{2} \d{2})? - ([^/]+?)\.\w+$', '\g<1>', newtitle, flags=re.IGNORECASE)

        # Date 2
        newtitle = re.sub('.*?/' + showname + '(?: \(\d{4}\))? - \d{4}-\d{2}-\d{4}(?: \d{2} \d{2} \d{2})? - ([^/]+?)\.\w+$', '\g<1>', newtitle, flags=re.IGNORECASE)

        if newtitle == episode.locations[0]:
            print('Unable to determine newtitle.  Exiting.')
            quit()
    
        if newtitle != episode.title:
            print('Old Title: ' + episode.title)
            if dryrun:
                print('New Title: ' + newtitle)
                print('Update required (Dry Run).')
                updaterequired += 1
            else:
                episode.batchEdits()
                episode.editTitle(newtitle, locked=True).editSortTitle(newtitle, locked=True)
                episode.saveEdits()
                print('New Title: ' + episode.title)
                print('Episode updated successfully.')
                updated += 1
                
            print()
        else:
            updatenotrequired += 1
            if verbose:
                print('Old Title: ' + episode.title)
                print('New Title: ' + newtitle)
                print('No update required.')
                print()

    print()
    print('==================================================')
    print('Show Name: ' + showname)
    print('Total Episodes: ' + str(total))
    if dryrun:
        print('Update Required: ' + str(updaterequired))
    else:
        print('Updated: ' + str(updated))
    print('Update NOT Required: ' + str(updatenotrequired))
    print('==================================================')
    print()
