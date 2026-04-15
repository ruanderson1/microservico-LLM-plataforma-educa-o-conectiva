from fastapi import APIRouter, HTTPException
from schemas.student import StudentReportRequest, StudentReportResponse
from schemas.class_ import ClassReportRequest, ClassReportResponse
from schemas.student import StudentReportRequest, StudentReportResponse
from services.student_report_service import generate_student_report
from services.class_report_service import generate_class_report

router = APIRouter(prefix="/reports")

@router.post("/student", response_model=StudentReportResponse)
async def student_report(request: StudentReportRequest):
    try:
        return await generate_student_report(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/class", response_model=ClassReportResponse)
async def class_report(request: ClassReportRequest):
    try:
        return await generate_class_report(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
