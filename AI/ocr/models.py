# Copyright 2024 HaUI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, List, Union
from pydantic import BaseModel

# Output model for the API response
class OCRResult(BaseModel):
    adress: Union[str, List[str]] = None
    birth: Union[str, List[str]] = None
    brand: Union[str, List[str]] = None
    gender: Union[str, List[str]] = None
    name: Union[str, List[str]] = None
    phone: Union[str, List[str]] = None
