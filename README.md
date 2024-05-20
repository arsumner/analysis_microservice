# analysis_microservice

To REQUEST data from this microservice:

1. Ensure that pyzmq is installed and imported into your program with the following import statement:

      import zmq

2. Connect to the zmq socket:
   
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:xxxx")

  Connect to a local host port or another port that you define in the client (main program) and the server (microservice).

3. Input sent to microservice is in JSON dictionary format:

    { "season: season, "round": num_round) where season represents year and round represents round in that specified year
   

To RECEIVE data from the microservice you:

Data will be returned in a JSON list of names of top 3 winners of the specified race.


TEST PROGRAM:

import zmq

 ZeroMQ client connection
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
     sends season and round for particular race winners query
    socket.send_json(message)

     receives output from microservice
    winners = socket.recv_json()
    return winners






UML sequence diagram showing how requesting and receiving data works:


<img width="785" alt="Screenshot 2024-05-19 at 11 20 08 PM" src="https://github.com/arsumner/analysis_microservice/assets/122269006/3a3ab16f-b7af-426b-8eff-25a508069546">
