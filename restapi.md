1. pip install

```bash
$pip install djangorestframework
```

2. app 추가

```python
INSTALLED_APPS = [
    'rest_framework',
    'musics',
]
```



```bash
$python manage.py dumpdata musics
```

* json 형태로 출력

```bash
$python manage.py dumpdata musics > musics
```

* json 파일을 생성, 보기않좋아, 한 줄로

```bash
python manage.py dumpdata --indent 2  musics
```

* json 파일을 생성하고 보기좋게 나열되어있다.



GET reviews/ 리뷰 목록

POST reviews/ 리뷰 등록하기

GET reviews/1 1번 리뷰 가져오기

PUT reviews/1 1번 리뷰 수정하기

DELETE reviews/1 1번 리뷰 삭제하기



GUI(Graphic User Interface)

그래픽 - 유저랑 상호작용하는 인터페이스

CLI(Command Line Interface)

명령어 인터페이스

API(Application Programming Interface)

프로그래밍으로 인터페이스