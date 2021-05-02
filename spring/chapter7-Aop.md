## AOP

- Aspect Oriented Programming
- 공통 관심 사항(cross-cutting concern)과 핵심 관심 사항(core concern) 분리하고 공통 관심 사항을 한군데 모아서 처리하는 방식
> 공통 관심 사항이란 일반적으로 여러 메서드에 들어가는 공통 기능 등을 말하며 이런 사항을 모아두지 않으면 중복 코드도 많고 수정시 과도한 반복작업과 누락등의 문제가 있다.
- 자바에서 AOP 구현체로는 AspectJ, Spring AOP가 있다.
    - Spring AOP가 실행속도, 기능적인 측면에서 밀리나, 쓰기 편하고 웬만한 기능은 있어서 성능 이슈나, 추가 기능이 필요할때만 AspectJ를 쓰는게 좋다고 한다.

```java
// AOP 코드 예시

@Component
@Aspect  // AOP로 쓰기 위한 어노테이션
public class TimeTraceAop {
	@Around("execution(* hello.hellospring..*(..))")
	public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
		long start = System.currentTimeMillis();
		System.out.println("START: " + joinPoint.toString());
		try {
			return joinPoint.proceed();  // 다음 메서드로 진행시키는 메서드
		} finally {
			long finish = System.currentTimeMillis();
			long timeMs = finish - start;
			System.out.println("END: " + joinPoint.toString()+ " " + timeMs + "ms");
	 	}
	}
}

```

### AOP 주요용어

- Target : 부가기능을 부여할 대상.
- Advice : 언제 공통 관심 기능을 핵심 로직에 적용할 지를 정의.
- Joinpoint : Advice를 적용 가능한 지점.
- Pointcut : Joinpoint의 부분 집합으로 실제 Advice가 적용되는 Joinpoint
- Weaving : Aspect가 지정된 객체를 새로운 프로시 객체로 생성하는 과정
- Aspect : 여러 객체에 공통으로 적용되는 기능
- Proxy : 타겟을 감싸서 타겟의 요청을 대신 받아주는 Wrapping Object

### Advice 종류

- Before : 메서드 호출 전
- After Returning : 메서드가 익셉션 없이 실행된 이후
- After Throwing : 메서드를 실행하는 도중 익셉션이 발생한 경우
- After : 익셉션 발생 여부에 상관없이 메서드 실행 후
- Around : 메서드 실행 전, 후 또는 익셉션 발생 시점

### Pointcut 명시 방법 (어떤 메서드의 지점인지 설정)

1. execution 명시자

    ```java
    1. execution(public void set*(..))
    	-> public void : 리턴 타입이 void인 public 메서드 중
    	-> set* : 메서드 이름이 set으로 시작하고
    	-> (..) : 파라미터가 0개 이상인 메서드
    2. execution(* chap07..*.*(..))
    	-> * chap07.. : chap07 패키지와 그 하위 패키지에 있는
    	-> *.*(..) : 파라미터가 0개 이상인 메서드
    3. execution(* get*(*))
    	-> 이름이 get으로 시작하고 파라미터가 한 개인 메서드
    ```

2. within 명시자

    ```java
    1. within(com.edu.aop.SomeService)
     - com.edu.aop.SomeService 인터페이스의 모든 메서드
    2. within(com.edu.aop.*)
     - com.edu.aop 패키지의 모든 메서드
    3. within(com.edu.aop..*)
     - com.edu.aop 패키지 및 하위 패키지의 모든 메서드
    ```

3. bean 명시자

    ```java
    bean(someBean)
     - 이름이 someBean인 빈의 모든 메서드
    bean(some*)
     - 빈의 이름이 some으로 시작하는 빈의 모든 메서드

    // 빈의 이름 대소문자에 주의할 것
    ```

### Weaving과 Proxy

- Weaving에는 Compile-time Weaving, Load-time weaving, Run-time weaving  ****세가지 방식이 존재 한다.
- 스프링 AOP에서는 CGLIB Proxy, JDK Dynamic Proxy를 이용한 Run-time weaving 방식을 제공한다.
- Proxy 객체가 Weaving을 통해 생성된다.
- 타겟이 호출될 때 바로 타켓에 접근하는게 아니라 proxy객체를 거쳐서 간접적으로 타겟에 접근하게 된다.

### 추가사항

- 일반적으로는 @EnableAspectJAutoProxy 어노테이션을 선언해줘야 @Aspect 기능이 활성화되는데 @SpringbootAplication으로 인해 생략해도 된다.
    - @SpringbootAplication안에 @EnableAutoConfiguration이 있고 이 어노테이션은 스프링부트가 클래스패스에서 찾은 빈들을 설정하게 한다. 따라서 스프링이 @Aspect를 보고 프록시방식으로 사용하게 해주기 때문에 @EnableAspectJAutoProxy가 생략가능하다.
