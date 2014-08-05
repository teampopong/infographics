# Infographics on Korean Politics


## Dependencies
- PIL

## Run

그림을 그리기 위해 아래를 실행한다.

    $ ./build.py [graphic_code]


### List of graphic codes

- [2014/timeline](2014/timeline/drawing.png)


## How to contribute

### 코드

1. 각 연도의 폴더 아래 각 인포그래픽 관련 폴더 생성 (ex: `2014/timeline/`)
1. 인포그래픽을 생성하는 코드는 `draw.*`에 저장하고 실행권한 부여 (ex: `2014/timeline/draw.r`)
1. 인포그래픽은 `drawing.png`로 저장 (ex: `2014/timeline/drawing.png`)

### 데이터

1. 최대한 공개 데이터/API 사용
1. 1이 불가능한 경우,
    - 재사용 가능한 데이터: [data-for-rnd](http://github.com/teampopong/data-for-rnd)에 업로드 후 링크
    - 재사용이 어려운 데이터: 해당 폴더 내에 저장


## License

CC by 4.0
(unless otherwise noticed)
