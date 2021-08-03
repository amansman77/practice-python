# practice-python
파이썬을 공부하는 공간입니다.

## 컨테이너 환경

빌드
```
docker build -t ho/python:directory .
```

구동
```
docker run -it --rm -v /home/hshwang/workspace/github/practice-python:/home --name ho-python ho/python:directory
```