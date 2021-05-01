## ComponentScan

- 스프링이 스캔 대상 클래스를 검색해서 빈으로 자동 등록해주는 기능
- 컴포넌트 스캔 기능을 사용하면 설정 클래스에 빈으로 등록하지 않아도 원하는 클래스를 빈으로 등록할 수 있으므로 설정 코드가 크게 줄어든다
- @Autowired 사용이 필수적이다. (스프링이 자동으로 빈을 등록하기 때문에 의존 관계 주입도 자동으로 되는 기능이 필요하므로)

## 스캔 대상 지정

- 클래스에 @Component 어노테이션을 쓰면 해당 클래스는 스캔 대상으로 지정된다.
- @Component 어노테이션 외에도 스캔 대상에 포함되는 어노테이션들이 존재한다.
- @Controller, @Service, @Repository, @Configuration
    - 각 어노테이션에 대한 추가 설명

## @ComponentScan 어노테이션

- 스캔 대상으로 표시된 객체들을 스프링 빈으로 등록하려면 설정 클래스에 @ComponentScan 어노테이션을 적용해야한다.
- 스캔 기본 범위는 @ComponentScan 어노테이션을 적용한 설정 클래스의 패키지 부터 하위 패키지들을 스캔하여 대상 객체들을 스프링 빈으로 등록한다.
- @ComponentScan의 속성값을 수정하여 스캔 범위를 조정할 수 있다.
- 범위에 해당하지 않는곳에선 @Component 어노테이션을 써도 스프링 빈으로 자동 등록되지 않는다.

## 스캔 범위를 지정하는 Filter

- includeFilters : 컴포넌트 스캔 대상을 추가로 지정한다.
- excludeFilters : 컴포넌트 스캔에서 제외할 대상을 지정한다.

```java
@InComponent
public class BeanA { ... }

@ExComponent
public class BeanB { ... }

@Configuration
@ComponentScan(
	includeFilters = @Filter(type = FilterType.ANNOTATION, classes = InComponent.class),
	excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = ExComponent.class)
)
class ComponentFilterAppConfig { ... }

// BeanA타입의 beanA만 스프링 빈으로 등록된다.
```

### 1. **FilterType**

- ANNOTATION: 기본값, 애노테이션을 인식해서 동작한다.
    ex) org.example.SomeAnnotation
- ASSIGNABLE_TYPE: 지정한 타입과 자식 타입을 인식해서 동작한다.
    ex) org.example.SomeClass
- ASPECTJ: AspectJ 패턴 사용
    ex) org.example..*Service+
- REGEX: 정규 표현식
    ex) org\.example\.Default.*
- CUSTOM: TypeFilter라는 인터페이스를 구현해서 처리
    ex) org.example.MyTypeFilter

### 2. **권장 사항**

- includeFilters의 경우 @Component로 충분하기 때문에 쓰는 일이 거의 없다.
- excludeFilters의 경우 간혹 사용하긴하나 많이 쓰지 않는다.
- 최근 스프링 부트는 컴포넌트 스캔을 기본으로 제공하기에 속성값을 수정 하는 것보다 기본 설정에 맞추어 사용 하는 것을 권장한다.

## 컴포넌트 스캔시 충돌

### 1. **자동 등록 vs 자동 등록**

- 다른 패키지에 동일한 이름의 클래스가 스캔 대상일 경우, 또는 상속 객체로 인해 발생할 수 있는 문제
- 둘 중 하나에 명시적으로 빈 이름을 지정해서 이름 충돌을 피해야한다.

### 2. **자동 등록 vs 수동 등록**

- 스프링에선 자동 등록하는 빈과 수동 등록하는 빈의 이름이 충돌할 경우 수동 등록한 빈이 우선시 된다.
    (오버라이딩 되어 에러가 발생하지 않는다.)

- 스프링부트에선 에러를 던지도록 설정되어 있다.
    (spring.main.allow-bean-definition-overriding 값의 기본값이 false되어 있다. true로 변경하면 스프링과 동일하게 처리된다.)
