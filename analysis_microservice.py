import zmq
import requests


def winners_query(season, num_round):
    response = requests.get(f'https://ergast.com/api/f1/{season}/{num_round}/results.json')

    if response.status_code == 200:
        data = response.json()

        winners = []
        for i in range(0, 3):

            driver_id = data['MRData']['RaceTable']['Races'][0]['Results'][i]
            driver = f"{driver_id['Driver']['givenName']} {driver_id['Driver']['familyName']}"
            winners.append(driver)

        return winners

    else:
        return ["Bad request: Unable to fetch data."]


# ZeroMQ server connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5623")

while True:
    message = socket.recv_json()
    season = message['season']
    num_round = message['round']

    winners = winners_query(season, num_round)

    socket.send_json(winners)

