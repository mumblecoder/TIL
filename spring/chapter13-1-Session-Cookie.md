## 세션과 쿠키

- 웹 서비스는 클라이언트와 서버와의 관계를 유지하지 않는 Stateless 기반의 HTTP 프로토콜로 사용자와 통신한다.
- Stateless 상태를 해결하는 두 가지 방식이 있는데 바로 세션(Session)과 쿠키(Cookie)다.
- 두 방식 모두 사용자와 서버의 연결 상태를 유지해주는 방법으로, 세션은 서버에서 정보를 관리하는 반면 쿠키는 사용자에 측에서 정보를 관리하는 데 차이가 있다.

## Session (세션)

### 1. 세션에 대해서

- 세션은 서버 측에서 관리한다.
- 서버에서는 클라이언트를 구분하기 위해 세션 ID를 부여하며 웹 브라우저가 서버에 접속해서 브라우저를 종료할 때까지 인증상태를 유지한다.
- 접속 시간에 제한을 두어 일정 시간 응답이 없다면 정보가 유지되지 않게 설정 할 수 있다.
- 정보를 서버에 두기 때문에 쿠키보다 보안에 좋지만, 사용자가 많아질수록 서버 메모리를 많이 차지한다.
- 클라이언트가 Request를 보내면, 해당 서버의 엔진이 클라이언트에게 유일한 ID를 부여하는 데 이것이 세션ID다.
- 스프링 MVC에서 세션은 HttpServletRequest 혹은 HttpSession을 사용해서 구현할 수 있다.

```java
// 세션에 정보 저장
@PostMapping("/login")
public String login(HttpServletRequest req, User user) {
    HttpSession session = request.getSession();
    User user = service.login(user);
    session.setAttribute("user", user);
    ...
}

// 세션에서 정보 조회
@PostMapping("/modify")
public String modify(HttpServletRequest req, User user) {
    HttpSession session = request.getSession();
    User user = session.getAttribute("user", user);
    modifyUser = service.modify(user);
    ...
}

// 세션 정보 삭제
@deleteMapping("/logout")
public String logout(HttpServletRequest req, User user) {
    HttpSession session = request.getSession();
    User user = service.logout(user);
    session.invalidate();
    ...
}
```

### 2. 세션의 동작 방식

1. 클라이언트가 서버에 접속 시 세션 ID를 발급받는다.
2. 클라이언트는 세션 ID를 쿠키로 저장해서 가지고 있는다.
3. 클라이언트는 서버에 요청할 때, 세션 ID를 서버에 전달해서 사용한다.
4. 서버는 세션 ID를 전달 받아서 별다른 작업없이 세션 ID로 세션에 있는 클라언트 정보를 가져옵니다.
5. 클라이언트 정보를 가지고 서버 요청을 처리하여 클라이언트에게 응답합니다.

## Cookie (쿠키)

### 1. 쿠키에 대해서

- 쿠키는 클라이언트(브라우저) 로컬에 저장되는 키와 값이 들어있는 작은 데이터 파일.
- 사용자 인증이 유효한 시간을 명시할 수 있으며, 유효 시간이 정해지면 브라우저가 종료되어도 인증이 유지된다는 특징이 있습니다.
- 쿠키는 클라이언트의 상태 정보를 로컬에 저장했다가 참조한다.
- 클라이언트에 300개까지 쿠키저장 가능, 하나의 도메인당 20개의 값만 가질 수 있음, 하나의 쿠키값은 4KB까지 저장.
- Response Header에 Set-Cookie 속성을 사용하면 클라이언트에 쿠키를 만들 수 있다.
- 쿠키는 사용자가 따로 요청하지 않아도 브라우저가 Request시에 Request Header를 넣어서 자동으로 서버에 전송한다.

### 2. 쿠키의 동작 방식

1. 클라이언트가 페이지를 요청하면 서버에서 쿠키를 생성한다
2. HTTP 헤더에 쿠키를 포함 시켜서 응답한다
3. 브라우저가 종료되어도 쿠키 만료 기간이 있다면 클라이언트에서 보관하고 있다
4. 같은 요청을 할 경우 HTTP 헤더에 쿠키를 함께 보낸다
5. 서버에서 쿠키를 읽어 이전 상태 정보를 변경 할 필요가 있을 때 쿠키를 업데이트 하여 변경된 쿠키를 HTTP 헤더에 포함시켜 응답한다

## 세션과 쿠키의 차이점

- 세션도 결국 쿠키를 사용하기 때문에 역할이나 원리가 비슷하다.
- 가장 큰 차이점은 쿠키는 서버의 자원을 전혀 사용하지 않으며, 세션은 서버의 자원을 사용한다.
- 보안 면에서 세션이 더 우수하며, 요청 속도는 쿠키가 세션보다 빠르다. (세션은 서버의 처리가 필요하기 때문)
- 쿠키는 클라이언트 로컬에 저장되기 때문에 변질되거나 request에서 스니핑 당할 우려가 있어서 보안에 취약하지만 세션은 쿠키를 이용해서 sessionid 만 저장하고 그것으로 구분해서 서버에서 처리하기 때문에 비교적 보안성이 좋습니다.
- 쿠키, 세션 모두 만료 시간을 정할 수 있지만 쿠키는 파일로 저장되기 때문에 브라우저를 종료해도 계속해서 정보가 남아 있을 수 있지만, 세션은 브라우저가 종료되면 만료시간 상관없이 삭제된다.
