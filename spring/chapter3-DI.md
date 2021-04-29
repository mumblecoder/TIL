## DI

- DI = Dependency Injection(의존 주입)

```java
// DI를 적용하지 않은 방식
public class MemberRegisterService {
	private MemberDao memberDao = new MemberDao();
	...
}

// DI를 적용한 방식 (생성자 주입)
public class MemberService {
	private MemberDao memberDao;

	public MemberService(MemberDao memberDao) {
		this.memberDao = memberDao;
	}
}
```

- 애플리케이션 실행 시점(런타임)에 외부에서 실제 구현 객체를 생성하고 클라이언트에 전달해서 클라이언트와 서버의 실제 의존관계가 연결 되는 것을 의존관계 주입이라 한다.
- 객체 인스턴스를 생성하고, 그 참조값을 전달해서 연결된다.
- 의존관계 주입을 사용하면 클라이언트 코드를 변경하지 않고, 클라이언트가 호출하는 대상의 타입 인스턴스를 변경할 수 있다.

## DI의 장점

1. 결합도를 낮추면서 유연성과 확장성을 향상 시켜준다.
2. 재사용성을 높여주고 코드를 단순화 시켜준다.

```java
// 1) DI를 적용하지 않은 방식
public class MemberService {
	private MemberDao memberDao = new MemberDao();
}

public class SignupService {
	private MemberDao memberDao = new MemberDao();
}
...

// 2) DI를 적용한 방식
public class Create {
	MemberDao memberDao = new MemberDao();
	SignupService signupService = new SignupService(memberDao);
	MemberService memberService = new MemberService(memberDao);
	...
}

// 1)의 경우 memberDao를 쓰는 클래스 수(n)만큼 memberDao를 생성해야하고 변경될 경우 n번 수정해야한다.
// 2)의 경우 memberDao를 1번 생성하여 주입하므로 변경되더라도 생성한 1곳만 수정하면 된다.
```

## 스프링 DI

- 스프링은 필요한 객체를 생성하고 생성한 객체에 의존을 주입한다.
- 스프링을 이용하여 DI를 적용할때는 어떤 객체를 생성하여 의존을 어떻게 주입할지를 정의한 설정 파일을 만들어야 한다.

```java
@Configuration
public class Config {

	@Bean
	public MemberDao memberDao() {
		return new MemberDao();
	}

	@Bean
	public SignupService signupService() {
		return new SignupService(memberDao());
	}
}
```
