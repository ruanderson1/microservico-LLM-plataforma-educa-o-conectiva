from pydantic import BaseModel, Field
from typing import List

class Activity(BaseModel):
    tipo: str
    nota_maxima: float
    pontuacao: float
    peso: float
    observacoes: str

class StudentReportRequest(BaseModel):
    student_id: int
    periodo_referencia: str
    observacao_professor: str
    observacao_pais: str
    atividades: List[Activity]

class StudentReportResponse(BaseModel):
    student_id: int
    periodo_referencia: str
    desempenho_geral: str
    evolucao_recente: str
    dificuldades_aprendizagem: str
    pontos_fortes_aprendizagem: str
    estado_emocional_geral: str
    engajamento: str
    risco_desempenho_baixo: str
    risco_desengajamento: str
    necessita_intervencao: bool
    resumo_llm: str
    recomendacao_para_professor: str
    recomendacao_para_pais: str
    plano_acao_sugerido: str
