from datetime import datetime, timedelta
from slack_sdk import WebClient 


def update_slack_status():
    """
    Gets BSSID of AP that WiFi interface is connected to

    :param os: string of a current OS platform
    :param interface: name of WiFi interface
    :return: string bssid of WiFi AP that interface is connected to
    """


# docs: https://api.slack.com/methods/users.profile.set


    expiration_timestamp = datetime.utcnow()
    expiration_timestamp = expiration_timestamp + timedelta(seconds=4*60)
    expiration_timestamp = expiration_timestamp.timestamp()

    PAYLOAD = {
        "profile": {
            "status_text": "riding a train",
            "status_emoji": ":troll:"
            "status_expiration": expiration_timestamp
        } 
    }

    client = WebClient(token=slack_api_token) # TODO API token
    response = client.users_profile_set

"""
PROFILE="{\"status_emoji\":\"$EMOJI\",\"status_text\":\"$TEXT\"}"
RESPONSE=$(curl -s --data token="$TOKEN" \
    --data-urlencode profile="$PROFILE" \
    https://slack.com/api/users.profile.set)
if echo "$RESPONSE" | grep -q '"ok":true,'; then
    echo "${green}Status updated ok${reset}"
else
    echo "${red}There was a problem updating the status${reset}"
    echo "Response: $RESPONSE"
fi
"""
