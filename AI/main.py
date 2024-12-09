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

from fastapi import FastAPI
from digital_sig.main_digital_sig import app as digital_sig_router
from ocr.main_ocr import app as ocr_router

app = FastAPI(root_path="/ai")

# Thêm các router vào ứng dụng chính
app.include_router(ocr_router, prefix="/ocr", tags=["OCR APIs"])
app.include_router(digital_sig_router, prefix="/digital-sig", tags=["Digital Signature APIs"])

