import miio

"""
mirobo --ip 192.168.1.6 --token 42783931395962556764314e6e6b4475 start
mirobo --ip 192.168.1.6 --token 42783931395962556764314e6e6b4475 zoned-clean [23279,26675,26679,29325,1]


docker run --init -d --name="home-assistant" -e "TZ=Asia/Jerusalem" -v C:\workspace\home-assistant\config:/config -p 8123:8123 homeassistant/home-assistant:stable
"""
IP = "192.168.1.6"
TOKEN = "42783931395962556764314e6e6b4475"

vac = miio.Vacuum(IP, token=TOKEN, start_id=0, debug=5)
print(vac.sound_volume())
#vac.goto(23279, 26675)
#vac.home()
#vac.find()
vac.fresh_map(2)