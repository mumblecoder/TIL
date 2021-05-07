## 날짜 클래스

[NAVER D2](https://d2.naver.com/helloworld/645609)

### 1. Date, Calendar

- 자바 8 버전이 나오기 전까지 주로 쓰인 날짜 클래스이다.
- 다음 문제점들로 인해 사용을 지양하고 있다.
    1. 불변 객체가 아니다
        - set 메서드 제공된다. 여러곳에서 공유 되었을때 원치 않는 결과값을 얻는 문제가 발생한다.
    2. int 상수 필드의 남용

        ```java
        cal.add(Calendar.DATE, 1); // 정상적으로 하루를 더하는 방식 
        cal.add(Calendar.DECEMBER, 1) // 잘못된 사용이지만 컴파일 과정에서 오류가 발생하지 않는다.
        ```

    3. 헷갈리는 월 지정
        - cal.set(2020, 8, 30) 을 하면 2020-09-30을 얻게된다.
    4. 일관성 없는 요일 상수
        - Calendar 일요일 상수값은 1, Date 일요일 상수값은 0 이다.
    5. 오류에 둔감한 timezone 지정

        ```java
        TimeZone.getTimeZone("Asia/Seoul"); // 존재하는 TimeZone
        TimeZone.getTimeZone("Seoul/Asia"); // 존재하지 않는 TimeZone
        // 타임존이 존재하지 않아도 에러가 발생하지 않는다. 
        ```

    6. Java.util.Date의 하위 클래스 문제
        - eqauls 대칭성 문제가 있는데, 하위 클래스 timestamp에 대하여 객체 a.equal(b) true인데 b.eqauls(a) false가 나오는 문제가 있다.

### 2. java.time 패키지

- 자바 8 버전에 추가된 패키지. 날짜 데이터 처리에 유용한 클래스들이 있다.
    - 주요 클래스들 간단 설명
        - LocalDate : 달력 시스템에서 시간대가 없는 날짜만을 표기하는 클래스 (UTC x)
        - LocalTime : 달력 시스템에서 시간대를 표기하는 클래스 (UTC x)
        - LocalDateTime : 날짜와 시간을 모두 표기 할때 사용되는 클래스
        - ZonedDateTime : ISO-8601 달력 시스템에서 정의하고 있는 타임존의 날짜와 시간을 저장하는 클래스
        - DateTimeFormatter : java.time에 대한 형식 (날짜 → 텍스트), 변환 (텍스트 → 날짜)을 나타내는 클래스
        - Duration : 시간을 초 단위 및 나노초 단위로 측정하는 클래스
        - Period : 시간을 년,월,일로 측정하는 클래스
        - TemporalAdjuster : 현재 날짜를 기준으로 년도의 첫 번째 일, 마지막 일, 월의 첫 번째 일, 마지막일, 지난 요일 및, 돌아오는 요일 등 상대적인 날짜로 변경하게 하는 클래스
- 다음 이유들로 인해 사용이 권장되고 있다.
    1. 불변 객체
        - 변경 메소드를 호출해도 새 인스턴스를 리턴하여 기존 인스턴스는 유지된다.
    2. 직관적인 날짜 계산
        - plusDays() 처럼 직관적인 메서드로 인해 쓰기 편함
    3. 오류 처리
        - 월이 잘못 설정(13월)되거나, 잘못된 타임존이 설정되면 에러 발생
    4. 다양한 캘린더 시스템 운용
        - ISO-8601 표준 시스템을 준수하지 않는 캘린더도 운용 가능.

## 날짜값 변환

### 1. SimpleDateFormat

- Date ↔ String 변환시 사용.
- Date 클래스처럼 점점 안쓰는 추세

### 2. DateTimeFormatter

- java.time 패키지 안에 있는 클래스로 java.time 패키지내의 날짜 객체들을 변환시 사용

```java
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
LocalDateTime now = LocalDateTime.now();
System.out.println(now.format(dtf));  // 2021-05-03 17:40:07
```

### 3. @DateTimeFormat

- 커맨드 객체내 필드에 @DateTimeFormat 어노테이션을 사용하면 특정 형식의 문자열을 날짜형으로 변환해준다.

```java
public class DateBean {
	@DateTimeFormat(pattern = "yyyyMMdd")
	private LocalDate nowDate;
	@DateTimeFormat(pattern = "HHmmss")
	private LocalTime nowTime;
	@DateTimeFormat(pattern = "yyyyMMdd HHmmss")
	private LocalDateTime nowDateTime;	
} 
```
