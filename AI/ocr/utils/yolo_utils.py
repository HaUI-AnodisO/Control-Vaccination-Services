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

from ultralytics import YOLO
from PIL import Image
from typing import Dict

def load_yolo_model(model_path: str) -> YOLO:
    """Load YOLO model."""
    return YOLO(model_path)

def get_label_map() -> Dict[int, str]:
    """Define label map for YOLO."""
    return {
        0: "adress",
        1: "birth",
        2: "brand",
        3: "gender",
        4: "name",
        5: "phone",
        6: "stamp"
    }
