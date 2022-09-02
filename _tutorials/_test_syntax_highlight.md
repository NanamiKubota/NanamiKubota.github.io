---
title: "test syntax"
layout: single
permalink: /tutorials/syntax
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2022-03-08
#classes: wide
---

```java
int total = 0;
for(int i = 0; i < list.length; i++)
{	total += list[i];
System.out.println( list[i] );
}
return total;
Scala
  def findNums(n: Int): Iterable[(Int, Int)] = {

    // a for comprehension using two generators
    for (i <- 1 until n;
         j <- 1 until (i-1);
         if isPrime(i + j)) yield (i, j)
  }
```

```cpp
#include <iostream>
using namespace std;

int main() 
{    
    cout << "Size of char: " << sizeof(char) << " byte" << endl;
    cout << "Size of int: " << sizeof(int) << " bytes" << endl;
    cout << "Size of float: " << sizeof(float) << " bytes" << endl;
    cout << "Size of double: " << sizeof(double) << " bytes" << endl;

    return 0;
}
```

```python
# line comment
v = 1
s = "string"

for i in range(-10, 10):
    print(i + 1)

class LinkedList(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```

```ruby
require "gem"

string = "base16"
symbol = :base16
fixnum = 0
float  = 0.00
array  = Array.new
array  = ['chris', 85]
hash   = {"test" => "test"}
regexp = /[abc]/

# This is a comment
class Person
  
  attr_accessor :name
  
  def initialize(attributes = {})
    @name = attributes[:name]
  end
  
  def self.greet
    "hello"
  end
end

person1 = Person.new(:name => "Chris")
print Person::greet, " ", person1.name, "\n"
puts "another #{Person::greet} #{person1.name}"
```