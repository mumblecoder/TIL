## ThreadLocal
- 자바 ThreadLocal 클래스는 오직 한 쓰레드에 의해 읽고 쓰여질 수 있는 변수를 생성할 수 있도록 한다.
- 두 쓰레드가 같은 코드를 실행하고 이 코드가 하나의 ThreadLocal 변수를 참조하더라도, 이 두 쓰레드는 서로의 ThreadLocal 변수를 볼 수 없다
- 글자 그대로 쓰레드의 지역변수이다.

![ThreadLocal](/img/java/ThreadLocal.png)

## 주요 용도
1. 사용자 인증정보 전파 
	- Spring Security에서는 ThreadLocal을 이용해서 사용자 인증 정보를 전파한다.
2. 트랜잭션 컨텍스트 전파 
	- 트랜잭션 매니저는 트랜잭션 컨텍스트를 전파하는 데 ThreadLocal을 사용한다.
3. 쓰레드에 안전해야 하는 데이터 보관
4. 이 외에도 쓰레드 기준으로 동작해야 하는 기능을 구현할 때

## 주의점
- Thread Pool을 통해 thread를 재사용할 경우 한번 쓴 ThreadLocal 객체는 remove() 를 통해 비워줘야 한다. 그러지 않으면 다음번 해당 스레드가 사용될 때 올바르지 않은 데이터를 참조 할 수도 있다.
- 메모리 누수의 주범이 됨으로 주의해서 사용해야 한다.

## 사용법
1. ThreadLocal 객체를 생성한다.
2. set() 메서드를 이용해서 현재 쓰레드의 로컬 변수에 값을 저장한다.
3. get() 메서드를 이용해서 현재 쓰레드의 로컬 변수 값을 읽어온다.
4. remove() 메서드를 이용해서 현재 쓰레드의 로컬 변수 값을 삭제한다.


###출처 
- [ThreadLocal 사용법과 활용](https://javacan.tistory.com/entry/ThreadLocalUsage)
- [ThreadLocal](https://getinterviewinfo.wordpress.com/2014/09/04/thread-local/)
