[Interview.postman_collection.json](https://github.com/user-attachments/files/17960219/Interview.postman_collection.json)
Created a collection in Postman, with which you may test the APIs method that I've created for this interview test. 

Example URLs (server needs to be running in django):

GetbyId: http://127.0.0.1:8000/tasks/getid?id=10
GetALL: http://127.0.0.1:8000/tasks/getlist
Insert (need to send Body): http://127.0.0.1:8000/tasks/insert
DeletebyID: http://127.0.0.1:8000/tasks/deleteid?pk=30
UpdatedbyID: http://127.0.0.1:8000/tasks/updateid

Sample Update Body JSON:
{
"pk":43,
"title":"manu1",
"description":"task4description",
"status":"Active"
}
