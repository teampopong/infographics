# Infographics on Korean Politics


Names/handles in parentheses are contributers.

### Published

None

### Queue

- [2014/timeline](2014/timeline): 역대 국회, 대통령 한 눈에 보기 (@e9t)
- [2014/nbills](2014/nbills): 국회별 발의 의안 수 (@sairion, @e9t, @cornchz)
- [2014/rerun](2014/rerun): 국회의원 재출마, 재선출 비율 (@e9t)
- [2015/sankey](2015/sankey): 의안 처리 프로세스 (@e9t)
- [2015/us](2015/us/drawing.png): 미국 의회 vs 한국 국회 (@e9t)
- [2015/count](2015/count): 대수별 국회의원 수 추이 (@e9t)
- [2015/billtypes](2015/billtypes): 국회의 의안 뜯어보기 (@e9t)
- [2015/trashed](2015/trashed): 나날이 증가하는 폐기물들 (@e9t)
- [2015/proposers](2015/proposers): 법은 누가 만드나요? {@e9t)
- [2015/billlife](2015/billlife): 발의자 타입별 의안 처리 기간 (@e9t)
- [2015/billlife2](2015/billlife2): 대수별 의안 처리 기간 (@e9t)
- 전세계 국가별 여성 국회의원 비율
- 현직 국회의원 연령대


## Dependencies

### Python
- numpy
- pandas
- PIL
- pylab

### R
- ggplot2
- timeline

## Run

그림을 그리기 위해 아래를 실행한다.

    $ ./build.py [graphic_code]


## How to contribute

### 코드

1. 각 연도의 폴더 아래 각 인포그래픽 관련 폴더 생성 (ex: `2014/timeline/`)
1. 인포그래픽을 생성하는 코드는 `draw.*`으로 저장하고 실행권한 부여 (ex: `2014/timeline/draw.r`)
1. 인포그래픽은 해당 폴더에 저장 (ex: `2014/timeline/drawing.png`)
1. `README.md`의 [List of graphic codes](#list-of-graphic-codes)에 인포그래픽 코드(`graphic_code`) 추가

### 데이터

1. 최대한 공개 데이터/API 사용
1. 1이 불가능한 경우,
    - 재사용 가능한 데이터: [data-for-rnd](http://github.com/teampopong/data-for-rnd)에 업로드 후 링크
    - 재사용이 어려운 데이터: 해당 폴더 내에 저장


## License

CC by 4.0
(unless otherwise noticed)
