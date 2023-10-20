# Receipt-Processor

Built avaliable via Dockerfile, simply use command below under current diretory:

```bash
docker build -t dockerdjango .
```

after build the docker image, use this command:

```bash
docker run -d -p 8000:8000 --name myapp dockerdjango
```