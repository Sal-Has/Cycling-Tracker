import requests
from datetime import datetime

pixel_endpoint ='https://pixe.la/v1/users'

USERNAME = 'salim3375'
TOKEN = '123fdjgfuydcdcd'


user_params = {
'token' :TOKEN,
'username':USERNAME,
'agreeTermsOfService':'yes',
'notMinor':'yes',
}

# response=requests.post(url=pixel_endpoint,json=user_params)

# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"


graph_config={
    'id':'graph2',
    'name':'Running Graph',
    'unit':'Km',
    'type':'float',
    'color':'ajisai',
}


headers={

    'X-USER-TOKEN':TOKEN
}


# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
today_date=datetime.now()
today_date=today_date.strftime("%Y%m%d")
# pixel_config={
#     'date':today_date,
#     'quantity':input('How many kilometres did you cycle? ')
# }
post_pixel_endpoint = f"{graph_endpoint}/graph2"

# response=requests.post(url=post_pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)


update_pixel_endpoint=f"{post_pixel_endpoint}/{today_date}"

update_pixel_config = {
    'quantity':'4.5'

}

# response=requests.put(url=update_pixel_endpoint,json=update_pixel_config,headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{post_pixel_endpoint}/{today_date}"

response=requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)












