## 자동 주입

- 스프링에서는 자동으로 의존하는 객체를 주입해주는 기능이 있다. 이를 자동 주입이라고 부르는데 자동주입을 설정하려면 @Autowired 어노테이션을 사용하면 된다.

## 자동 주입 방식

### 1. 생성자 주입

```java
@Component
public class OrderService {
	private final DiscountPolicy discountPolicy;
	
	@Autowired
	public OrderService(DiscountPolicy discountPolicy) {
		this.discountPolicy = discountPolicy;
	}
}

// 생성자 호출시점에 딱 1번만 호출되는 것이 보장된다.
// 불변, 필수 의존 관계에 사용
```

### 2. 수정자 주입(setter 주입)

```java
@Component
public class OrderService {
	private DiscountPolicy discountPolicy;
	
	@Autowired
	public void setDiscountPolicy(DiscountPolicy discountPolicy) {
		this.discountPolicy = discountPolicy;
	}
}

// 선택, 변경 가능성이 있는 의존 관계에 사용
```

### 3. 필드 주입

```java
@Component
public class OrderService {
	@Autowired
	private DiscountPolicy discountPolicy;
}

// 코드가 간결하여 좋아보이지만 외부에서 변경이 불가능해 테스트하기가 힘들다.
// DI 프레임워크가 없으면 아무것도 할 수 없다.
// 웬만하면 자제하고 설정 파일이나 실제 코드와 관련없는 테스트 코드에서만 쓰는게 좋다.
```

### 4. 일반 메서드 주입

```java
@Component
public class OrderService {
	private DiscountPolicy discountPolicy;
	
	@Autowired
	public void init(DiscountPolicy discountPolicy) {
		this.discountPolicy = discountPolicy;
	}
}

// 일반적으로 잘 사용하지 않는다.
```

### 5. 생성자 주입을 사용하자

- 대부분 의존관계 주입은 한번 일어나면 변경될 일이 없기때문에 생성시 1번만 호출되는 생성자 주입을 써야 불변하게 설계 할 수 있다.
- 생성자 주입 사용시엔 주입데이터가 누락되면 컴파일 오류가 발생하여 누락여부를 알기 쉽다.
- final 키워드 사용이 가능하다. 생성자에서 혹시라도 값이 설정되지 않는 오류를 컴파일 시점에 막아준다.
- 롬복을 사용하면 더욱 간결한 코드를 짤 수 있다.

## 자동 주입 옵션 처리

- 주입할 스프링 빈이 없어도 동작해야 할 때가 있는데 @Autowired만 사용하면 자동 주입 대상이 없으면 오류가 발생한다.
- 이 오류를 해결할 방법으로 아래 3가지가 있다.

### 1. @Autowired 어노테이션의 required 속성을 false로 변경

- 주입할 빈이 없을 경우 에러를 발생하지 않고 값도 할당하지 않는다
- setter 메서드에서 쓴 경우 setter 메서드 자체가 동작하지 않는다.

```java
@Autowired(required = false)
private MemberPrinter memberPrinter;

@Autowired(required = false)
public void setMemberPrinter(MemberPrinter memberPrinter) {
	this.memberPrinter = memberPrinter;
	System.out.println("setter method");  // 주입할 빈이 없는 경우 실행되지 않음.
}
```

### 2. 자동 주입 대상 타입을 Optional로 설정

- 빈이 존재하지 않으면 값이 없는 Optional을 인자로 전달하고 에러는 발생하지 않는다.

```java
@Autowired
Optional<MemberPrinter> memberPrinter;

@Autowired
public void setMemberPrinter(Optional<MemberPrinter> memberPrinter) { ... }
```

### 3. @Nullable 어노테이션 사용

- 빈이 존재하지 않으면 에러를 던지지 않고 인자값으로 null을 전달한다.

```java
@Autowired
@Nullable
MemberPrinter memberPrinter;

@Autowired
public void setMemberPrinter(@Nullable MemberPrinter memberPrinter) { ... }
```

@Autowired(required = false) 방법은 값 할당 자체를 하지 않지만, Optional의 경우 값이 없는 Optional을, @Nullable의 경우 null값을 할당한다.

## 자동 주입시 발생 가능한 문제

### 1. 일치하는 빈이 없는 경우

- NoSuchBeanDefinitionException 발생. 해당 타입의 빈이 없다는 에러메시지가 출력

### 2. 자동 주입 대상에 일치하는 빈이 2개 이상

- NoUniqueBeanDefinitionException 발생. 해당 타입 빈이 2개 이상 발견되었다는 에러메시지가 출력

## 해결 방법

### 예제

```java
// DiscountPolicy를 상속받은 FixDiscountPolicy, RateDiscountPolicy 클래스
@Component
public class FixDiscountPolicy implements DiscountPolicy {}

@Component
public class RateDiscountPolicy implements DiscountPolicy {}
```

```java
@Autowired
private DiscountPolicy discountPolicy;

// 위와 같이 주입받으면 NoUniqueBeanDefinitionException 발생.
// DiscountPolicy대신 하위 타입을 지정하면 이 상황에선 해결할 수 있지만 DIP를 위배하고 유연성이 떨어진다.
// 이름만 다르고, 완전히 똑같은 타입의 스프링 빈이 2개 있을 때 해결이 안된다
```

### 1. @Autowired 필드 명 매칭

```java
@Autowired
private DiscountPolicy rateDiscountPolicy;

// 필드명 매칭은 먼저 타입 매칭을 시도시 결과에 여러 빈이 있을 때 추가로 동작하는 기능이다.
// 에러없이 자동 주입이 된다.
```

### 2. @Qualifier → @Qualifier끼리 매칭 → 빈 이름 매칭

- @Qualifier는 추가 구분자를 붙여주는 방법이다. 추가 구분자일뿐 빈 이름은 변경되지 않는다.

```java
@Component
@Qualifier("mainDiscountPolicy")
public class FixDiscountPolicy implements DiscountPolicy {}
```

```java
@Autowired
public SaleService(MemberRepository memberRepository,
 @Qualifier("mainDiscountPolicy") DiscountPolicy) {
	this.memberRepository = memberRepository;
	this.discountPolicy = discountPolicy;
}
```

- @Qualifier 로 주입할 때 @Qualifier("mainDiscountPolicy")를 못 찾으면 mainDiscountPolicy라는 이름의 스프링 빈을 추가로 찾는다.

### 3. @Primary 사용

- @Primary는 우선순위를 정하는 방법이다. @Autowired시 여러 빈이 매칭되면 @Primary가 우선권을 가진다. (단, @Qualifier와 순위가 충돌할 경우 @Qualifier가 우선권이 높다.)

```java
@Component
@Primary
public class FixDiscountPolicy implements DiscountPolicy {}

@Component
public class RateDiscountPolicy implements DiscountPolicy {}
```

```java
@Autowired
private DiscountPolicy discountPolicy;

// 에러가 발생하지 않고 FixDiscountPolicy타입이 주입된다.
```
