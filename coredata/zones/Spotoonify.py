from otp.ai import MagicWordGlobals
import sys
import spotipy
import spotipy.util as util

@magicWord (category = CATEGORY_USER, types = [])
def spotify():
	token = util.prompt_for_user_token(username, scope)
	if token:
		sp = spotipy.Spotify(auth=token)
		user_playlist(username, playlist_id=None, fields=None)
		