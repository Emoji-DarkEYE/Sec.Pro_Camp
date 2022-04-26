import requests

# UrlBox: https://api.telegram.org/bot2044060648:AAEw59K7XRkf4oAhoSvP5WPTvLG7FErnR7Q/sendmessage?chat_id=1341257291&text=plase sub my channel on youthub
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
        sending_url = ("https://api.telegram.org/bot2044060648:AAEw59K7XRkf4oAhoSvP5WPTvLG7FErnR7Q/sendmessage?chat_id=1341257291&text="+pm)


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










        


