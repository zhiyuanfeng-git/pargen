# pargen
This package implements an event-driven system using the observer pattern,aiming to decouple code.

# Description
It contains a parser and a generator. In the parser module, you can perform some 'parser actions'. After these actions are performed successfully, a generator will get a notification. Then you could do some 'generator actions' in the generator module. You do not need to involve the notification method to a generator explicitly, it's called implicitly. Accordingly, you can pay more attention to the interesting features.

# Usage
You could define a class to inherit from Parser, then overwrite the parse method to perform some processes. After that, a class that is a subclass of Generator will receive the notification. Then you need to overwrite the generate method to perform some actions. 
Note that the class Event is accountable for passing parameters from the parse method to the generator method.

# Example
The package named [filesgenerator](https://github.com/zhiyuanfeng-git/filesgenerator) is an example using pargen.

# License
This source code is licensed under the Apache License, Version 2.0 found in the LICENSE and NOTICE file in the root directory of this source code.

# Version
The current version is '0.0.1'.