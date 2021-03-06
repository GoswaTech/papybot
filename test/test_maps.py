import pytest

from maps import MapsApi


class TestMaps:
    """ Class Maps search informations about the place. It can give :
        - the location (long, lat)
        - the city name """

    PLACE = "Tour Eiffel"
    LOCATION = {'longitude': 0.42, 'latitude': 0.42}
    MAPS = "Paris"

    def test_init(self):

        maps_api = MapsApi(self.PLACE)

        assert maps_api.place == self.PLACE


    """ MapsApi get location of a given place """
    def test_get_location(self, monkeypatch):
        """ get_location() return a dict with geopoints """

        def mock_get_geopoint(mock_self):
            return self.LOCATION

        maps_api = MapsApi(self.PLACE)

        monkeypatch.setattr(MapsApi, 'get_geopoint', mock_get_geopoint)

        geopoint = maps_api.get_location()

        assert geopoint == self.LOCATION


    def test_get_location_no_location(self, monkeypatch):
        """ get_location() return a dict with geopoints """

        def mock_get_geopoint(mock_self):
            return None

        maps_api = MapsApi(self.PLACE)

        monkeypatch.setattr(MapsApi, 'get_geopoint', mock_get_geopoint)

        geopoint = maps_api.get_location()

        assert "NO_LOCATION" in maps_api.errors
