import json
from . import client, create_token, reset_db
from unittest import mock
from unittest.mock import patch

class TestMockWeatherBit():
	def mocked_requests_get(*args, **kwargs):
		class MockResponse:
			def __init__(self, json_data, status_code):
				self.json_data = json_data
				self.status_code = status_code

			def json(self):
				return self.json_data

		if len(args) > 0:
			if args[0] == "https://api.weatherbit.io/v2.0/ip":
				return MockResponse({
							"latitude": "-12123.123124",
							"longitude": "123123.123123",
							"city": "Malang",
							"organization": "AS7713 PT Telekomunikasi Indonesia",
							"timezone": "Asia/Jakarta"
						}, 200)
			elif args[0] == "https://api.weatherbit.io/v2.0/current":
				return MockResponse({
					"data": [{"datetime":"2019-12-19:15","temp": 23}]
				}, 200)
		else:
			return MockResponse(None, 404)

	# @patch.object(PublicGetCurrentWeather,'get')
	@mock.patch('requests.get',side_effect=mocked_requests_get)
	def test_weather(self, test_reqget_mock, client):
		token = create_token(True)

		data = {
            "ip":"125.160.201.41"
        }
		res = client.get('/weather/ip',query_string= data,
		headers={'Authorization': 'Bearer ' + token})

		res_json = json.loads(res.data)

		assert res.status_code == 200
