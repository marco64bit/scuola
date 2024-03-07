

azienda para


customer

    profilo

    weekly_tracks
    
    play
    
API

@app("/v1/customer/{id}/", method="GET")
def get_customer(id):
    pass

PUT "/v1/customer/{id}/"

POST "/v1/play/"
{
    "mood": ""
    "wheater": "",
    ...
}

    

-----------------------------------------


cliente

App Android

    libs/
        para_client/
            client.py
    view/
        homepage
    model/
    controller/
    


client.py 


    class Variation():
        
        mood: str
        wheater: str

    class Para():
        
        def __init__(self, client_key, client_secret):
            self.client_key = client_key
            self.client_secret = client_secret
            
        def play(self, variation_obj: Variation):
            ...
            variation_obj.mood
            ...
            requests.post("/v1/play", variation_obj)
            ...
        
        def get_customer(self):
            requests.get(f"/v1/customer/{self.id}")
            pass
        
        def update_customer():
            pass
        
        def weekly_track_list():
            pass

-----------

from para_client impot Para

para = Para(client_key="asjdoiasjdiasdjas", client_key="pippo")

para.play(para.Variation(mood="happy"))



client () -> --- rete --- (codice) -> server
pc -> () -> usb -> () -> arduino


function client_play()
    ...
    write("Play: mood={}"%s)
    
    response = read()
    response.split(":")[0]
    



function play() {}
    mood = read(sensor1)
    client_play(mood)
}