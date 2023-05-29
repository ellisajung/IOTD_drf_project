# IOTD

## Item of the Day


## Start Routine

### 가상환경 재구성

    poetry shell

#### window기준

    source .venv/scripts/activate

#### mac은 해당 path를 찾아주어 적용하면 됨

    poetry env info --path

### 종속패키지 설치

#### requirements사용시

    pip install -r requirements.txt

#### poetry 사용시

    poetry update package

    poetry install

#### requirements에서 poetry로 이동시

    cat requirements.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add

#### poetry에서 requirements로 이동시

    poetry export -f requirements.txt --output requirements.txt

### 시크릿키 발급 및 인증용 이메일정보 추가

    py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

https://djecrety.ir/

    touch secrets.json

    {
      "SECRET_KEY": "해당 키",
      "EMAIL_HOST_USER": "이메일주소",
      "EMAIL_HOST_PASSWORD": "비림번호"
    }

#### db.sqlite3에 migrate

    py manage.py migrate

#### 이슈체크

    py manage.py check

#### 관리자 계정생성 및 서버테스트

    py manage.py createsuperuser

    py manage.py runserver

---

# Project Purpose

yolov5를 활용한 자동태그가 달리는 패션커뮤니티

## Usage Language & FrameWork

Backend - Python, Django Rest Framework

Frontend - Vanilla JS

## Usage Management Method

requirements.txt

poetry

json

## Usage Package

    python = "^3.11"
    django = "^4.2"
    djangorestframework-simplejwt = "^5.2.2"
    djangorestframework = "^3.14.0"
    django-cors-headers = "^3.14.0"
    pillow = "^9.5.0"
    pytest-django = "^4.5.2"
    coverage = "^7.2.6"
    pytest-cov = "^4.1.0"
    pytest-factoryboy = "^2.5.1"
    pytest-faker = "^2.0.0"

