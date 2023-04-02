# fuzzing-project

## Updating packages

### Python
Before installing new packages open the corresponding environment:<br>
```
source applications/<app_folder>/env/bin/activate
```
To then save newly installed packages do fom the <app_folder>:<br>
```
pip freeze > requirements.txt
```
To install new packages from collaborator:
```
pip install -r requirements.txt
```
## Docker
Navigate to application/<app_folder> and then build if neccesary with: <br>
```
docker image build -t flask_app .
```
Then to run it: <br>
```
docker run -p 5000:5000 -d flask_app
```
To list current containers:<br>
```
docker ps
```
To stop a container:
```
docker stop <container_name>
```