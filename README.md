# pargen
This package implements an event-driven system using the observer pattern,aiming to decouple code.

# Description
It contains a parser and a generator. In the parser module, you can perform some 'parser actions'. After these actions are performed successfully, a generator will get a notification. Then you could do some 'generator actions' in the generator module. You do not need to involve the notification method to a generator explicitly, it's called implicitly. Accordingly, you can pay more attention to the interesting features.

# Usage
  ###### Step 1
  Import necessary modules
  ```python
    from pargen.parsers import Parser
    from pargen.generators import Generator
    from pargen.event import Event,EventType
    from pargen.status import Status
  ```
  ###### Step 2
  Define a class called EventTypeA, inherit from EventType.
  Define a class called EventA, inherit from Event.
  ```python
  class EventTypeA(EventType):
    NONE = 0
    TYPEA = 1

  class EventA(Event):
    def __init__(self):
        super().__init__(EventTypeA.TYPEA)
        self.data = None
    
    def cleanup(self):
        self.data = None
  ``` 
  ###### Step 3
  Define a class called ParserA, inherit from Parser.
  Override parse method to implement some 'parse' actions.
  ```python
  class ParserA(Parser):
    def __init__(self, event, generator):
        Parser.__init__(self, event, generator)

    def parse(self, *args) -> Status | None:
        if args[0] is None:
            return Status.ERROR_INTERRUPTED
        self._event.data = args[0]
        print(f'Parse args: {args}')
  ```
  ###### Step 4
  Define a class called GeneratorA, inherit from Generator.
  Override generate method to implement some 'generate' actions.
  ```python
  class GeneratorA(Generator):
    def generate(self, event):
        data = event.data
        print(f'Generate data: {data}')
  ```
  ###### Step 5
  Call the ParserA to perform the 'parse' actions.
  ```python
  event = EventA()
  generator = GeneratorA()
  parser = ParserA(event, generator)
  parser('parameter1','parameter2')
  ```


# Example
The package named [filesgenerator](https://github.com/zhiyuanfeng-git/filesgenerator) is an example using pargen.

# License
This source code is licensed under the Apache License, Version 2.0 found in the LICENSE and NOTICE file in the root directory of this source code.

# Version
The current version is '0.0.1'.