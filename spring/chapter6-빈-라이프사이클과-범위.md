## 스프링 빈의 Event Life Cycle

- 스프링 컨테이너 생성 → 스프링 빈 생성 → 의존관계 주입 →초기화 콜백 → 사용 → 소멸전 콜백 → 스프링 종료
    - 초기화 콜백 : 빈이 생성되고, 빈의 의존관계 주입이 완료된 후 호출
    - 소멸전 콜백 : 빈이 소멸되기 직전에 호출

## 스프링이 빈 생명주기 콜백을 지원하는 3가지 방법

### 1. **인터페이스 InitializingBean, DisposableBean**

- 수정이 불가능한 외부 라이브러리에는 인터페이스를 사용할 수 없다
- 스프링 전용 인터페이스라서 해당 코드가 스프링 전용 인터페이스에 의존한다.
- 초기화, 소멸 메서드의 이름을 변경할 수 없다.
- 이 방식은 초창기에 사용한 방식이고 지금은 거의 사용하지 않는다.

```java
public class MemberDao implements InitializingBean, DisposableBean {

	@Override
	public void afterPropertiesSet() throws Exception {
		connect();
	}	

	@Override
	public void destroy() throws Exception {
		disConnect();
	}

	...
}
```

### 2. **@Bean 어노테이션의 속성 (initMethod, destroyMethod)**

- 빈 등록할때 @Bean 어노테이션의 initMethod, destroyMethod 속성을 이용하여 초기화/소멸 메서드를 지정할 수 있다.
- 스프링 빈이 스프링 코드에 의존하지 않는다.
- 코드가 아닌 설정 정보를 사용하기 때문에 수정 불가한 외부 라이브러리 객체에도 적용할 수 있다.
- destroyMethod에는 특별한 기능이 있다. 기본값이 "(inferred)" (추론)로 등록되어 있어서 'close', 'shutdown' 라는 이름의 메서드를 자동으로 호출해준다.
- 추론 기능을 원치 않을 경우 빈 문자열("")로 설정해주면 된다.

```java
@Configuration
public class Config {
	
	// 이 경우 destroyMethod 속성을 입력하지 않아도 자동으로 close()메서드를 호출한다.
	@Bean(initMethod = "init", destroyMethod = "close")
	public MemberDao memberDao() {
		return new MemberDao();
	}
}

public class MemberDao {
	public init() {
		...
	}
	
	public close() {
		...
	}
	...
}
```

### 3. **@PostConstruct, @PreDestroy 어노테이션**

- 스프링에서 권장하는 방식
- 초기화 메서드에 @PostConstruct, 소멸메서드에 @PreDestroy 어노테이션을 사용하면 된다.
- 스프링에 종속적인 기술이 아니라 자바 표준이다.
- 수정이 불가한 외부라이브러리의 경우 사용할 수 없다. 이런 경우엔 2번 방법으로 해야한다.

```java
public class MemberDao {
	@PostConstruct
	public init() {
		...
	}
	
	@PreDestroy
	public close() {
		...
	}
	...
}
```

## Bean Scope

- 스프링 빈은 기본적으로 싱글톤 스코프로 생성되어 스프링 컨테이너 시작과 함께 생성되어 스프링 컨테이너가 종료될 때 소멸된다.
- 스코프는 말 그대로 빈이 존재할 수 있는 범위이며, 스코프 값을 수정하여 빈의 존재 범위를 수정할 수 있다.
- 스코프는 @Scope 어노테이션을 사용하여 적용할 수 있다.

### 1. **싱글톤 (singleton)**

- 기본 스코프 값으로, 스프링 컨테이너의 시작과 종료까지 유지되는 가장 넓은 범위의 스코프.

### 2. **프로토타입 (prototype)**

- 스프링 컨테이너는 프로토타입 빈의 생성과 의존관계 주입, 초기화까지만 처리하고 더는 관리하지 않는 매우 짧은 범위의 스코프이다.
- 프로토타입 빈을 관리할 책임은 프로토타입 빈을 받은 클라이언트에 있다. 그래서 @PreDestroy 같은 종료 메서드가 호출되지 않는다.

### 3. **웹 관련 스코프**

- request : 웹 요청이 들어오고 나갈때까지 유지되는 스코프
- session : 웹 세션이 생성되고 종료될때까지 유지되는 스코프
- application : 웹의 서블릿 컨텍스와 같은 범위로 유지되는 스코프

## 싱글톤과 프로토타입 스코프 혼용시 발생할 수 있는 문제

- 프로토타입 빈을 직접 조회하면 매번 다른 빈이 생성되어 조회되지만, 프로토타입 빈을 주입받은 싱글톤 객체를 조회할때는 프로토타입 빈이 새로 생성되지 않는다.
- 싱글톤 객체에서는 생성시 주입 받은 프로토타입 빈을 유지하고 있기 때문이다.

## DL 기능을 사용하여 문제 해결하기

- DL = Dependency Lookup (의존관계 조회(탐색))
- DL 기능을 제공하는 것들로는 ObjectFactory, ObjectProvider, JSR-330 Provider가 있다.

### 1. **ObjectFactory, ObjectProvider**

- 스프링 제공 기능이라 별도 라이브러리가 필요없고 스프링에 의존한다.
- ObjectProvider가 ObjectFactory를 상속받고, 편의 기능이 추가 되있어서 ObjectFactory는 거의 쓰이지 않는다.
- ObjectProvider 의 getObject() 를 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서 반환한다. (DL)

### 2. **JSR-330 Provider**

- JSR-330 자바 표준을 사용하는 방법이라 스프링 외 다른 컨테이너에서도 사용 가능하다.
- javax.inject:javax.inject:1 라이브러리를 추가해야한다.
- Provider의 get()을 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서 반환한다. (DL)
- get() 외에 추가 기능은 없다.
