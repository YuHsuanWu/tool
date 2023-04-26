import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--content", default="完成！", type=str, help="What content do you want to print")

args = parser.parse_args()

def lineNotifyMessage(token, msg):
  headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    
  payload = {'message': msg}
  r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
  return r.status_code
    
# 修改為你要傳送的訊息內容
message = f'\n{args.content}'
# 修改為你的權杖內容
token = ''

lineNotifyMessage(token, message)