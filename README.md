
![2팀 시연영상(배속)](https://github.com/user-attachments/assets/9ba46c27-a44d-49ae-876d-3dbe9107aa4b)


# DESKER 
**DESKER**는 데스크 셋업에 관한 정보를 공유하는 커뮤니티와 데스크 셋업에 관련 상품을 판매/구매할 수 있는 Django 프로젝트입니다.

[**Team Repositories**](https://github.com/DESKER-e/desker) 를 보려면 클릭하세요.

<br>

## 주요 개발 사항

**1.커뮤니티 게시판**
- 데스크셋업에 관한 정보 공유를 위한 커뮤니티 게시판 입니다.
- 게시글 작성 시, `DESKER`에서 판매되고 있는 상품 검색을 할 수 있습니다.
- 게시글 작성 시, `DESKER`에서 판매되고 있는 검색된 상품 선택 시, 게시글 상세에 상품링크를 걸 수 있습니다.
- 게시글 상세에서 보이는 상품링크 클릭 시, 해당 상품 상세페이지로 이동할 수 있습니다.
- 게시글 작성자를 팔로우 & 팔로우 취소할 수 있습니다.
- 게시글&댓글 수정은 작성자만 가능합니다.
- 게시글&댓글 좋아요 및 좋아요 취소는 작성자만 가능합니다.

<br>

**2.판매자 스토어페이지**
- 특정 판매자가 등록한 상품 리스트를 볼 수 있습니다.
- 상품을 카테고리 별로 선택하여 볼 수 있습니다.
- 커뮤니티 게시글에서 특정 판매자의 상품이 링크 되었을 경우 `스타일링샷` 리스트에 해당 게시글을 볼 수 있습니다.
- 구매자 고객일 경우, 특정 판매자 페이지에서 스토어찜 기능을 할 수 있습니다.

<br>

**3.홈페이지 (메인페이지)**
- 홈 탭에서 판매중인 상품을 볼 수 있습니다. 판매중인 상품은 카테고리 별로 선택하여 볼 수 있습니다.
- 커뮤니티 탭에서 최신 작성된 순으로 게시글을 볼 수 있습니다.
- 고객센터 탭에서 쇼핑몰에 관한 자주 묻는 질문, 1:1 질문하기 을 이용할 수 있습니다.
- 구매자회원과 판매자회원 마이페이지 탭 구분
  - 구매자회원과 판매자회원 별도 회원가입을 지원합니다.
  - **구매자회원 마이페이지 탭**
    - 나의 쇼핑, 구매내역, 장바구니
  - **판매자회원 마이페이지 탭**
    - 나의 스토어, 상품, 상품문의

<br>

## ERD
[**ERD**](https://www.erdcloud.com/d/2WNAohmnrMteJBife) 를 보려면 클릭하세요.

<br>

## 설치 및 실행 방법
**1.저장소 클론**
```
git clone https://github.com/kim-taeseong/desk_item_shop.git
cd desk_item_shop
```

**2.가상환경 설치 및 실행**
```
python -m venv desker
source momento/bin/activate  # mac
source momento\Scripts\activate  # window
```

**3.필요한 패키지 설치**
```
pip install -r requirements.txt
```

**4.데이터베이스 마이그레이션**
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic 
```

**5.서버실행**
```
python manage.py runserver
```

<br>

## 크레딧
이 프로젝트는 다음과 같은 오픈소스패키지를 사용합니다.
- python
- Django
- PostgreSQL
- Bootstrap5

<br>

## GitHub
`@anjiyoo`  ·  `@kim-taeseong`  ·  `@jongyongg`  ·  `@yeojin-0` 