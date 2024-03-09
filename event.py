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

from enum import Enum

class EventType(Enum):
    """Used to define the type of event"""
    pass

class Event:
    """Used to pass data between Parsers and Generators"""
    
    def __init__(self, event_type):
        self.event_type = event_type
    
    def cleanup(self):
        pass

    def __str__(self):
        return f"object:{id(self)},event_type:{self.event_type}"