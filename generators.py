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
from .observer import Observer

class Generator(Observer):
    """
    Serves as the base class for subclasses 
    that specifically perform generating operations.
    It will be notified by a parser after the parser
    performed the action successfully. 
    """

    def _update(self, event):
        self.generate(event)

    @abstractmethod
    def generate(self, event):
        """
        Performs the generating action.
        It would be called when the action of parsing via the Parser class is performed successfully.
        """
        pass