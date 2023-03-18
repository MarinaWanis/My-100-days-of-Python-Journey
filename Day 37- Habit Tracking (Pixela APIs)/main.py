import requests
import datetime

USERNAME="*********"
TOKEN="*****************"
GRAPH_ID ="***************"

todays_date = datetime.datetime.now()
formatted_date = todays_date.strftime("%Y%m%d")
# print(formatted_date)

pixela_endpoint="https://pixe.la/v1/users"

user_parameters={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
#--------------------------------Creating User----------------------------------------#
# response= requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

#--------------------------------Creating the graph------------------------------------#
graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

graph_header ={
    "X-USER-TOKEN": TOKEN
}

graph_parameters={
    "id":GRAPH_ID,
    "name":"Track Coding Graph",
    "unit":"hours",
    "type":"float",
    "color":"sora"
}
#
# response= requests.post(url=graph_endpoint, headers=graph_header,json=graph_parameters)
# print(response.text)


#---------------------------------Post a pixel in your graph--------------------------#
post_pixel_endpoint= f"{graph_endpoint}/{GRAPH_ID}"

add_pixel_parameters= {
    "date":formatted_date,
    "quantity":input("How many hours of coding did you spend today?")
}
response= requests.post(url=post_pixel_endpoint,headers=graph_header,json=add_pixel_parameters)
print(response.text)

#-----------------------------Update a pixel in your graph--------------------------#

update_pixel_endpoint= f"{post_pixel_endpoint}/{formatted_date}"

update_pixel_parameters={
    "quantity":"6.5",
}

# response = requests.put(url= update_pixel_endpoint,headers=graph_header,json=update_pixel_parameters)
# print(response.text)


#------------------------------Delete a pixel---------------------------------------#
delete_pixel_endpoint= f"{post_pixel_endpoint}/{formatted_date}"


# response = requests.delete(url= delete_pixel_endpoint,headers=graph_header)
# print(response.text)



