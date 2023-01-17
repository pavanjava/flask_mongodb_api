## Instruction document to run the project

- Asumption: Mongodb is already installed and running on port 27017 & docker is also installed in the host machine
- open the code base in your favourite IDE and run the server.py
- different endpoints are as below

  - `resource: /api/v1/employee, method: GET`
  - `resource: /api/v1/employee, method: POST`
  - `resource: /api/v1/project, method: GET`
  - `resource: /api/v1/project, method: POST`
- also run the below command to dockerize the project

  - `docker build -t <tag-name> .`
  - `docker run --name flask-api -p 3000:5000 <tag-name/image-name>`

- added swagger1.0 for auto api document generation
- after running the application please run 

  - `http:\\<host>:<port>\api/spec.json`