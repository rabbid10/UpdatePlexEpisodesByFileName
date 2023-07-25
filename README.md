# UpdatePlexEpisodesByFileName.py

This script will update the Plex database for specified 'TV Shows' to reflect the name of the episode defined in the file.

## Requirements
plexapi.server - https://github.com/pkkid/python-plexapi

## Usage
Create a separate file called `secrets.py` in the same folder as UpdatePlexEpisodesByFileName.py with the following structure:

### Secrets
``` Python
baseurl = 'http://LocalFQDNOfYourPlexServer:32400'
token = 'YourPlexToken'
```

### Shows
Update the `shownames` array with the name of the shows you want to update.

### Dry Run
It's recommended that you run the script once with `dryrun` set to `True` to make sure there won't be any unintended consequences.  Once you happy with the predicted ouptut, set `dryrun` to `False` and run the script again.

## Examples
 - `The Big Bang Theory (2007) - S01E01 - Pilot` => Pilot

 - `The Big Bang Theory (2007) - S01E02 - The Big Bran Hypothesis` => The Big Bran Hypothesis
