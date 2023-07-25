# UpdatePlexEpisodesByFileName.py

This script will update the Plex database for specified 'TV Shows' to reflect the name of the episode defined in the file.

## Requirements
plexapi.server - https://github.com/pkkid/python-plexapi

## Usage
Create a separate file called `secrets.py` in the same folder as UpdatePlexEpisodesByFileName.py with the following structure:

``` Python
baseurl = 'http://LocalFQDNOfYourPlexServer'
token = 'YourPlexToken'
```

## Examples
The Big Bang Theory (2007) - S01E01 - Pilot => Pilot
The Big Bang Theory (2007) - S01E02 - The Big Bran Hypothesis => The Big Bran Hypothesis