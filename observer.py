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

from abc import ABC,abstractmethod
from .reinforce import ReinforceList

class Observable:
    """This object can be observable by observers"""
    
    def __init__(self):
        self.observers = ReinforceList()

    def has(self, observer) -> bool:
        return self.observers.exist(observer)
    
    def attach(self, observer) -> bool:
        return self.observers.append(observer)
    
    def detach(self, observer) -> bool:
        return self.observers.remove(observer)

    def _dispatcher(self, event):
        for observer in self.observers.gen():
            observer._update(event)

class Observer(ABC):
    """Accountable for observing the state of observable objects changed"""

    @abstractmethod
    def _update(self, event):
        pass