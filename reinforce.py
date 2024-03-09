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

"""
Strengthen the implementation of some data structures.

"""

class ReinforceList():
    """
     Maintain a list and a dictionary,responsible for
     improving the search speed of the list.

     Similar to the newly OrderedDict or the dictionary of recent built-in versions.
     But considering the versatility of many versions, here implement a simple replacement solution. 
     [Maybe later would change to a stable official version.]
    """

    def __init__(self) -> None:
        self.__list = []
        self.__map = {}

    def exist(self, element):
        return id(element) in self.__map

    def append(self, element) -> bool:
        if self.exist(element):
            return False
        
        self.__list.append(element)
        self.__map[id(element)] = element
        return True

    def remove(self, element) -> bool:
        if not self.exist(element):
            return False
        
        del self.__map[id(element)]
        self.__list.remove(element)
        return True

    def clear(self):
        self.__list.clear()
        self.__map.clear()

    def empty(self) -> int:
        return self.size() == 0

    def size(self) -> int:
        return len(self.__list)

    def get(self):
        return self.__list

    def gen(self):
        for item in self.__list:
            yield item