## 필터와 인터셉터

- 공통 업무 처리를 위해 활용할 수 있는 방법들이다.
- 처리 순서는 Filter -> Interceptor -> AOP -> Interceptor -> Filter 순으로 이루어진다.
- Filter와 Interceptor은 Servlet 단위에서 이루어진다.

## 필터 (Filter)

### 1. 필터에 대해서

- 요청과 응답을 거르고 정제하는 역할을 한다.
- 필터는 스프링 컨텍스트 외부에 존재하여 스프링과 무관한 자원에 대해 동작한다.
- 서블릿 필터는 DispatcherServlet 이전에 실행이 되는데 필터가 동작하도록 지정된 자원의 앞단에서 요청내용을 변경하거나, 여러가지 체크를 수행할 수 있다.
- 자원의 처리가 끝난 후 응답 내용에 대해서도 변경하는 처리를 할 수 있다.
- 보통 web.xml에 등록하고, 일반적으로 인코딩 변환 처리, XSS방어 등의 요청에 대한 처리로 사용된다.

### 2. 필터 실행 메서드

- init() - 필터 인스턴스 초기화
- doFilter() - 실제 처리 로직
- destroy() - 필터 인스턴스 종료

## 인터셉터(Interceptor)

### 1. 인터셉터에 대해서

- 요청에 대한 작업 전/후로 가로챈다고 보면 된다.
- 스프링의 DistpatcherServlet이 컨트롤러를 호출하기 전, 후로 끼어들기 때문에 스프링 컨텍스트 내부에서 Controller(Handler)에 관한 요청과 응답에 대해 처리한다.
- 스프링의 모든 빈 객체에 접근할 수 있다.
- 인터셉터는 여러 개를 사용할 수 있고 로그인 체크, 권한체크, 프로그램 실행시간 계산작업 로그확인 등의 업무처리를 할 수 있다

### 2. 인터셉터 실행 메서드

- preHandler() - Controller 실행 전
- postHandler() - Controller 실행 후 view Rendering 실행 전
- afterCompletion() - view Rendering 이후
