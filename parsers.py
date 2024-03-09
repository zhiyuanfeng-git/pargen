# Copyright 2024 Feng ZhiYuan <feng.zhiyuan@outlook.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import abstractmethod
from .exception import DuplicateGenerator,DoesNotExistGenerator
from .observer import Observable
from .status import Status

class Parser(Observable):
    """
    Serves as the base class for subclasses 
    that specifically perform parsing operations.
    
    You need to pass a generator as a parameter in the constructor.
    And you could attach other generators via the attach method.
    """

    def __init__(self, event, generator):
        Observable.__init__(self)
        self._event = event
        self.attach(generator)

    def attach(self, observer) -> bool:
        success = super().attach(observer)
        if not success:
            raise DuplicateGenerator
        
        return success
    
    def detach(self, observer) -> bool:
        success = super().detach(observer)
        if not success:
            raise DoesNotExistGenerator
        
        return success

    def __call__(self, *args):
        self._event.cleanup()
        status_ret = self.parse(*args)
        
        if (status_ret is not None) and (status_ret.value < Status.SUCCESS.value):
            return
        
        self._dispatcher(self._event)

    def get_event(self):
        return self._event

    @abstractmethod
    def parse(self, *args) -> Status | None:
        """
        Performs the parsing action.
        The Parser class would notify all the Generator classes 
        that had attached to it when the parsing action is performed successfully.
        """
        pass
