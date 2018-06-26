# Java---My-learning-notes
learning java :-)

### python VS java
> https://www.rose-hulman.edu/class/cs/csse220/200830/web/Resources/Python_vs_Java.html

### java, get set methods
> https://stackoverflow.com/questions/36102768/java-get-set-methods
- To understand get and set, it's all related to how variables are passed between different classes.
- The get method is used to obtain or retrieve a particular variable value from a class.
- A set value is used to store the variables.
- The whole point of the get and set is to retrieve and store the data values accordingly.
Ex:
```
//here
```

### java packages
> https://beginnersbook.com/2013/03/packages-in-java/
```
package myPackage;

import outsidePackage.someClass;

```
### private static vs public static and final
> https://developer.salesforce.com/forums/?id=906F0000000AuyOIAS
- static : Static methods (and variables) can be used without instantiating a new instance of the class
- non-static : Non-static method (and variables) must have a new instance of the class instantiated in order to be used.  Typically these rely on data inside the class that then is refered to inside the class

> https://beginnersbook.com/2014/07/final-keyword-java-final-variable-method-class/
- final variables are nothing but constants.
- A final method cannot be overridden.
- We cannot extend a final class. 


### Annotations
> https://beginnersbook.com/2014/09/java-annotations/
- Java Annotations allow us to add metadata information into our source code, although they are not a part of the program itself. 
- An annotation always starts with the symbol @ followed by the annotation name. The symbol @ indicates to the compiler that this is an annotation.

### Constructor overloading 

### Interfaces
- Ex.
public interface Abc {
return-type method-name1(parameter-list);
}
- An interface is a contract (or a protocol, or a common understanding) of what the classes can do. 
- One of the main usage of interface is provide a communication contract between two objects.
- main use of interface is to facilitate polymorphism. 
- python does not have any equivalent of interfaces, The closest thing is probably the abstract base classes module, which allows you to define common methods for a set of classes.
- Ex.
 
class Abstract:
  def myFunc(self):
      raise NotImplementedError("The method not implemented")


### junit
> http://www.vogella.com/tutorials/JUnit/article.html#junit_intro
- Unit test : A unit test is a piece of code written by a developer that executes a specific functionality in the code to be tested and asserts a certain behavior or state.
- Integration / functional test : An integration test aims to test the behavior of a component or the integration between a set of components. Integration tests check that the whole system works as intended, therefore they are reducing the need for intensive manual tests.
- src/test/java - for test classes
- A JUnit test is a method contained in a class which is only used for testing. This is called a Test class. To define that a certain method is a test method, annotate it with the @Test annotation.
- You use an assert method, provided by JUnit or another assert framework, to check an expected result versus the actual result. 
- These method calls are typically called asserts or assert statements.

### gradle
> https://www.stubbornjava.com/posts/multi-project-builds-with-gradle-and-fat-jars-with-shadow
> https://docs.gradle.org/current/userguide/command_line_interface.html
- gradle/
The gradle/ directory is the default location for including gradle scripts.

- build.gradle
The build.gradle file is where we will load all plugins
This is also where we handle building our fat JAR using the Shadow JAR plugin

- ./gradlew clean

Uses your project's gradle wrapper to execute your project's clean task. Usually, this just means the deletion of the build directory.


###  uberJar, fatJar and shadowJar in Gradle?
There is no difference whatsoever. These terms are all synonyms of each other.

The term "uber-jar" may be more commonly used in documentations (take the maven-shade-plugin documentation for example) but "fat-jar" is also widely used.





