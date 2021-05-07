## Exception (예외)

- 예외는 에러의 일종이다.
- 예외가 발생할 것을 대비하여 미리 예측해 이를 소스상에서 제어하고 처리하도록 만드는 것이 예외 처리이다.
- 예외에는 일반예외(Exception)와 실행예외(RuntimeException)가 있다.

![예외 종류](/img/exception-type.png)

### 1. 일반 예외 (Exception, Checked Exception)

- 개발자가 반드시 예외 처리를 해야한다. 하지 않으면 컴파일 시점에서 오류가 발생한다.
- **대표적 일반 예외 종류**
    1. ClassNotFoundException
    2. NoSuchMethodException

### 2. 실행예외(RuntimeException, Unchecked Exception)

- 컴파일러가 체크 할 수 없는 에러. 실행되기 전까지는 에러 여부를 알 수 없다.
- 개발자의 경험에 의해 에러 처리 코드를 구현해야한다.
- **대표적 실행 예외 종류**
    1. NullPointerException
    2. ArrayIndexOutOfBoundsException
    3. NumberFormatExcpeion

## 예외 처리 방법

- 예외 처리 방법으로는 직접 처리하는 방법과 던지는 방법이 있다.
- 예외가 발생한 상황에 따라 던지기도, 직접 처리하기도 하니 상황에 맞춰 예외 처리 방법을 선택해야한다.

### 1. 예외 처리하기

- **try-catch (단건 예외 처리용)**

    ```java
    try {
    	// 로직 실행 코드
    } catch (NullPointerException e) {
    	// NullPointerException에 대한 처리
    } catch (Exception e) {
    	// Exception에 대한 처리
    }
    ```

    - try문 안에서 예외가 발생하면 해당 에러에 맞는 catch문이 에러를 처리한다.
    - catch문이 여러개 필요할 경우 작은 범위의 예외부터 작성해야한다.
        - 위에서 catch문 순서가 바뀌면 NullPointerException이 발생해도 Exception catch문에서 처리된다. (if-else문처럼 순서 중요)
- **@ExceptionHandler (컨트롤러내 예외 처리용)**

    ```java
    @Controller
    public class CustomController {
    	
    	@ExceptionHandler(RuntimeException.class)
    	public String handleRuntimeException() {
    		return "error/exception";
    	}	
    	...
    }
    ```

    - Controller, RestController에서만 @ExceptionHandler 어노테이션을 사용하여 에러를 처리할 수 있다.
    - CustomController내에서 RuntimeException이 발생하면 handleRuntimeException()이 에러를 처리한다.
    - @ExceptionHandler가 있는 컨트롤러에만 적용된다.
- **@ControllerAdvice (공통 예외 처리용)**

    ```java
    @ControllerAdvice("com.example.test")
    public class CustomExceptionHandler {
    	
    	@ExceptionHandler(RuntimeException.class)
    	public String handleRuntimeException() {
    		return "error/exception";
    	}	
    }
    ```

    - 해당 컨트롤러만 적용되던 @ExceptionHandler의 기능을 @ControllerAdvice를 사용하여 원하는 모든 컨트롤러에 적용시킬 수 있다.
    - @ControllerAdvice 어노테이션이 적용된 클래스는 지정한 범위 안의 컨트롤러에 공통으로 사용될 설정을 지정할 수 있다.
    - CustomExceptionHandler가 동작하려면 스프링에 빈으로 등록되야한다.

### 2. 예외 던지기

- throws 키워드를 사용해 예외를 상위 코드 블록으로 던질 수 있다.

```java
public String test2() throws Exception {
	...
}
```

- 결국 어디선가 처리해야 하는데 왜 상위로 던지는가?

    → 그럴만한 에러이기에. 사용자의 잘못으로 발생한 에러를 던지지 않고 조용히 서버에서 처리한다면 사용자는 계속 에러를 발생시킬것이다.

- 주의 사항
    - throws 절이 있는 메소드를 오버라이딩 할 때는 메소드에 선언한 예외보다 더 광범위한 검사형 예외(일반 예외)를 던질 수 없음
    - 부모 클래스의 메소드에 예외를 떠넘기는 throws 절이 없다면 자식 클래스의 메소드를 오버라이딩 할 때 어떤 예외도 떠넘길 수 없음.
    - 불필요한 예외 던지기는 위험하고, 디버깅을 어렵게 만들 수 있으니 잘 생각해보고 던져야 한다.
