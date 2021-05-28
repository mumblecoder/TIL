# Gradle 문법 정리

## build.gradle 파일

- gradle에서 빌드 작업에 필요한 기본 설정, 동작 등을 정의하는 파일

## plugins

- 프로젝트를 빌드하기 위해선 컴파일이나 jar 파일 생성 등의 여러 작업을 해야하는데 그런 작업들을 해주는 플러그인들을 지정하는 블록
- plugins 블록 안에 필요한 플러그인을 지정해주고 이런 플러그인들은 필요한 과정들을 task로 포함하고 있다
- 빌드시에는 필요한 모든 과정을 플러그인의 내부 task가 진행 해준다

```
plugins {
	id 'org.springframework.boot' version '2.3.1.RELEASE'
	id 'io.spring.dependency-management' version '1.0.9.RELEASE'
	id 'java'
}

```

## repositories

- 저장소 정보를 관리하는 property. 소프트웨어를 등록하여 관리하는 장소를 가리킨다.
- mavenCentral 또는 jCenter 등의 중앙 저장소를 사용해도 되고, 로컬 저장소를 사용해도 된다.

```java
repositories {
	mavenCentral()
}
```

## dependencies

- implementation : 컴파일 할 때 접근 가능한 라이브러리 설정
(implementation 대신 compile을 쓰기도 하는데 compile은 deprecated되었으니 implementation을 사용하는게 좋다)
- testImplementation : 테스트 컴파일 할 때 접근 가능한 라이브러리 설정
- compileOnly : 컴파일 시에만 사용한다는 의미
- runtimeOnly : 런타임 시에만 사용한다는 의미
- dependencies 추가 방법은 2가지가 존재하는데 후자는 축약형으로 의미 차이는 없으니 선호하는 방법으로 쓰면 된다.

```groovy
dependencies {
    compile group: 'org.hibernate', name: 'hibernate-core', version: '3.6.7.Final'
    // 짧게 쓰면 "group:name:version"
    compile 'org.hibernate:hibernate-core:3.6.7.Final'
}
```

## annotationProcessor

- lombok, querydsl 등의 annotation processor를 사용하려면 annotationProcessor 블록을 추가해야한다.
- 컴파일 클래스 경로를 annotation processor 클래스 경로와 분리하여 빌드 성능을 향상할 수 있다. (???)

```groovy
dependencies {
	annotationProcessor 'org.springframework.boot:spring-boot-configuration-processor'
	annotationProcessor 'org.projectlombok:lombok'
}
```

## buildscript

- 빌드하는 동안 필요한 처리를 모아놓는 곳
- 이 안에 dependencies, repositories가 포함 될 수 있다.

```groovy
buildscript {
    ext {
        springBootVersion = '2.1.3.RELEASE'
    }
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
        classpath "io.spring.gradle:dependency-management-plugin:1.0.6.RELEASE"
    }
}
```

## ext

- 이 블록은 gradle의 모든 task에서 사용할 수 있는 일종의 전역 변수를 선언하는 블록이라고 보면 된다.

## allprojects, subprojects, project

- 멀티 모듈일 경우 이 블록들을 사용한다.
- 해당 블록에 설정한 사항이 적용되는 범위는 allprojects(전체 프로젝트), subprojects(하위 프로젝트), project(해당 프로젝트)이다.

```groovy
allprojects {
    group 'com.example'
    version '1.0-SNAPSHOT'
}

subprojects {
    apply plugin: 'java'
    apply plugin: 'org.springframework.boot'
    apply plugin: 'io.spring.dependency-management'

    sourceCompatibility = 1.8

    repositories {
        mavenCentral()
    }

    dependencies {
        testCompile group: 'junit', name: 'junit', version: '4.12'
    }
}

project(':example') {
    dependencies {
        ....
    }
}
```

## task

- 사용자가 임의로 작성해서 사용 가능한 블록
- 다양한 기능을 수행 할 수 있고, 다양한 문법을 가지고 있다. 신입이 작성할 확률은 극히 적기 때문에 개념만 숙지
- 선언하면 커맨드 라인에서 task [task 이름]으로 사용할 수 있다.

```groovy
task exampleTest {
    println 'Hello World!'
}
```

## settings.gradle 파일

- 여러가지로 사용 가능하지만 가장 많이 쓰이는 용도는 멀티 모듈 사용시 설정하는 용도이다.

### 출처
- [https://webfirewood.tistory.com/129](https://webfirewood.tistory.com/129)
