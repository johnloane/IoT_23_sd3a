let aliveSecond = 0;
let heartbeatRate = 2000;
let myChannel = "johns_sd3a_pi";

let pubnub;

const setupPubNub = () => {
    // Update this block with your publish/subscribe keys
    pubnub = new PubNub({
        publishKey : "Your Publish key",
        subscribeKey : "Your subscribe key",
        userId: "device id"
    });

    // add listener
    const listener = {
        status: (statusEvent) => {
            if (statusEvent.category === "PNConnectedCategory") {
                console.log("Connected to PubNub");
            }
        },
        message: (messageEvent) => {
            if(messageEvent.message.motion){
                document.getElementById("motion_id").innerHTML = messageEvent.message.motion;   
            }
        },
        presence: (presenceEvent) => {
            // handle presence
        }
    };
    pubnub.addListener(listener);

    // subscribe to a channel
    pubnub.subscribe({
        channels: [myChannel]
    });
};

function publishUpdate(channel, message)
{
    pubnub.publish({
        channel: channel,
        message: message
    });
}

function time()
{
        let d = new Date();
        var currentSecond = d.getTime();
        if(currentSecond - aliveSecond > heartbeatRate + 1000)
        {
                document.getElementById("connection_id").innerHTML="Dead";
        }
        else
        {
                document.getElementById("connection_id").innerHTML="Alive";
        }
        setTimeout('time()', 1000);
}

function keepAlive()
{
        fetch('/keep_alive')
        .then(response=>{
                if(response.ok){
                        let date = new Date();
                        aliveSecond = date.getTime();
                        return response.json();
                }
                throw new Error("Server offline");
        })
        .then(responseJson => {
                if(responseJson.motion == 1){
                        document.getElementById("motion_id").innerHTML = "Motion Detected";
                }
                else{
                        document.getElementById("motion_id").innerHTML = "No Motion Detected";
                }
        })
        .catch(error=>console.log(error));
        setTimeout('keepAlive()', heartbeatRate);
}

function handleClick(cb)
{
        if(cb.checked)
        {
                value = "on";
        }
        else
        {
                value = "off";
        }
        publishUpdate(myChannel, {"buzzer": value});
}


