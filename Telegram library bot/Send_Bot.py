import requests

# UrlBox: https://api.telegram.org/bot???????????????????????????????????????/sendmessage?chat_id=?????????&text=plase sub my channel on youthub
# ContentTypeBox: 
# ContentDataBox: 
# HeadersBox: 
# RefererBox: 
# AgentList: Mozilla Firefox
# AgentBox: 
# VersionsList: HTTP/1.1
# MethodList: POST


def make_MES(messege):
    try:
        #set your tocken & chat ID
        pm = str(messege)
        sending_url = ("https://api.telegram.org/bot                    /sendmessage?chat_id=       &text="+pm)


        #data///
        Datadic = {"UrlBox" : sending_url,
            "AgentList": "Mozilla Firefox",
            "VersionsList": "HTTP/1.1",
            "MethodList": "GET"
                }

        # "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

        requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data = Datadic)
    except:
        print("You must apply the changes to the tool")










        


