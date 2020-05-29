import song
import serializers
song = song.Song('1', 'Water of Love', 'Dire Straits')
serializer = serializers.ObjectSerializer()
serializer.serialize(song, 'JSON')