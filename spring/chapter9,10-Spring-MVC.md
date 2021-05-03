## 스프링 MVC 동작 방식

![spring-mvc](/img/spring/spring-mvc.png)

1. 클라이언트에서 요청 전송
2. 요청 URL과 매칭되는 컨트롤러 검색
3. 전달 받은 컨트롤러에 처리 요청 위임
4. 컨트롤러의 알맞은 메서드를 호출해서 요청 처리
5. 컨트롤러의 실행 결과를 ModelAndView로 변환해서 전달
6. 컨트롤러의 실행 결과를 보여줄 View 검색
7. 응답 결과 생성 요청
8. 생성한 응답 결과를 클라이언트로 리턴

## 개념 & 역할 정리

### 1. DispatcherServlet

- Spring Framework가 제공하는 Servlet 클래스.
- 사용자의 요청을 받는, 프런트 컨트롤러와 연동되는 진입점 역할
- 기본적인 처리 흐름을 제어하는 사령탑 역할
- Dispatcher가 받은 요청은 HandlerMapping으로 넘어간다.

### 2. Handler

- 프레임워크 관점에서는 ’핸들러‘라고 부르지만, 개발자가 작성하는 클래스의 관점에서는 ’컨트롤러‘라고 한다.

### 3. HandlerMapping

- 사용자의 요청을 처리할 핸들러를 찾는다. 요청에 대응할 핸들러를 선택하는 역할
- 요청 url에 해당하는 Controller 정보를 저장하는 table을 가진다.
- 즉, 클래스에 @RequestMapping(“/url”) annotaion을 명시하면 해당 URL에 대한 요청이 들어왔을 때 table에 저장된 정보에 따라 해당 클래스 또는 메서드에 Mapping한다.

### 4. HandlerAdapter

- 핸들러 메서드를 호출하는 역할

### 5. ViewResolver

- Controller가 반환한 View Name(the logical names)에 prefix, suffix를 적용하여 View Object(the physical view files)를 반환한다.
    - ex) view name: home, prefix: /WEB-INF/views/, suffix: .jsp
    - /WEB-INF/views/home.jsp View에게 Controller에서 받은 Model을 전달
- 이 후에 해당 View에서 Model data를 이용하여 적절한 페이지를 만들어 사용자에게 보여준다.
