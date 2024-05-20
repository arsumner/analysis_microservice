# TEST PROGRAM:

import zmq

# ZeroMQ client connection
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5623")


def get_winners(season, num_round):
    """
    Test function to get winners of a race in JSON format from microservice.
    Must be passed the particular season/round that the microservice will return the winners for.
    """
    message = {
        "season": season,
        "round": num_round
    }
    # sends season and round for particular race winners query
    socket.send_json(message)

    # receives output from microservice
    winners = socket.recv_json()
    return winners


# test = get_winners(2008, 1)
# print(test)


