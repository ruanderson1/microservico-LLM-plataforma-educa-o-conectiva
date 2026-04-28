from pydantic import BaseModel
from typing import List, Union

class StudentSummary(BaseModel):
    student_id: Union[str, int]
    desempenho_geral: str
    engajamento: str
    risco_desengajamento: str
    dificuldades_aprendizagem: str

class ClassReportRequest(BaseModel):
    class_id: Union[str, int]
    periodo_referencia: str
    observacao_professor_turma: str
    students: List[StudentSummary]

class ClassReportResponse(BaseModel):
    class_id: Union[str, int]
    periodo_referencia: str
    desempenho_medio_turma: str
    principais_dificuldades_turma: str
    nivel_engajamento_turma: str
    risco_desengajamento_turma: str
    necessita_intervencao_coletiva: bool
    resumo_llm_turma: str
    recomendacao_para_professor_turma: str
    plano_acao_turma: str
