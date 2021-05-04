## 요청 매핑

### 1. @RequestMapping

- 경로, 메서드 등을 설정하여 요청 경로를 매핑 할 수 있다.
- 어노테이션의 속성
    1. value : 경로 값
    2. method : 요청 방식 
    3. headers : key-value 형식의 header 값

```java
@RequestMapping(method = RequestMethod.GET, 
	value = "/test",  headers = "content-type=text/plain")
public String test() {
    return "test";
}
```

### 2. @GetMapping / @PostMapping / ...

- 스프링 4.3 버전에 추가 된 것
- 접두사로 붙은 요청 방식만 처리할 수 있다.
- method 속성은 없고 그 외 속성은 @RequestMapping과 동일하다.

## 요청 파라미터 접근

### 1. HttpServletRequest

- 메서드의 파라미터로 HttpServletRequest 타입을 사용하면 getParameter() 메서드로 값을 구할 수 있다.

```java
@GetMapping
public String test(HttpServletRequest req) {
	String param = req.getParameter("test");
	...
}
```

### 2. @RequestParam

- 요청 파라미터의 개수가 많지 않을때 이 어노테이션을 사용하여 간단하게 요청 파라미터 값을 구할 수 있다.
- 어노테이션의 속성
    1. value : HTTP 요청 파라미터의 이름을 지정한다.
    2. required : 필수 여부를 boolean 값으로 지정. 이 값이 true일때 값이 없으면 익셉션이 발생한다.
    3. defaultValue : 요청 파라미터가 없을때 사용할 문자열 값을 지정한다.

    ```java
    @GetMapping
    public String test(
    	@RequestParam(required = true, value= "val") String param) {
    	service.test(val);
    	...
    }
    ```

### 3. 커맨드 객체

- 파라미터가 많을 경우엔 위 2가지 경우 모두 많은 코드를 필요로 한다. (하나씩 값을 다 구해야 하므로)
- 스프링에서는 **커맨드 객체(Command Object)**를 지원하여 **HTTP**에서 들어오는 각 속성값들을 자동적으로 커맨드 객체에 바인딩하여 처리한다.
- 커맨드 객체는 요청 파라미터들을 필드로 갖고 있고 setter 메서드가 구현되어 있어야 한다.

```java
@GetMapping
public String test(TestVO params) {
	String test = params.getTest;
	...
}
```

## 리다이렉트 처리

- 컨트롤러에서 특정 페이지로 리다이렉트 하고 싶을때는 "redirect: + 경로"를 뷰 이름으로 리턴하면 된다.
- ex. 현재 경로가 http://localhost:8080/test/register
    - redirect:/register/step1 (절대경로)

        → [http://localhost:8080/register/step1](http://localhost:8080/register/step1) 

    - redirect:register/step1 (상대경로)

        → http://localhost:8080/test/register/step1
