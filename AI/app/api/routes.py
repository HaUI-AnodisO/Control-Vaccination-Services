from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.gemini_service import generate_content, load_prompt
from app.utils.file_util import save_temp_image, delete_temp_image
from app.models.response_models import ResponseData
from app.services.parsing_service import parse_string_to_json

router = APIRouter()

# Load prompt content tại thời điểm khởi tạo
prompt_content = load_prompt()

@router.post("/generate-content", response_model=ResponseData)
async def generate_content_endpoint(image: UploadFile = File(...)):
    try:
        # Lưu ảnh tạm thời
        temp_image_path = save_temp_image(image)

        # Tạo nội dung
        result = generate_content(prompt_content, temp_image_path)

        # Xóa ảnh tạm
        delete_temp_image(temp_image_path)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
