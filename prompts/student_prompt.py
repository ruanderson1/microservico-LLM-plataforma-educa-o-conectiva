from schemas.student import StudentReportRequest
from typing import List

def build_student_prompt(request: StudentReportRequest) -> str:
    # Calculate weighted average and highlight scores
    activities = request.atividades
    total_weight = sum(a.peso for a in activities if a.nota_maxima > 0)
    weighted_sum = sum((a.pontuacao / a.nota_maxima) * a.peso for a in activities if a.nota_maxima > 0)
    weighted_avg = weighted_sum / total_weight if total_weight > 0 else 0
    
    low_scores = [a for a in activities if a.pontuacao / a.nota_maxima < 0.5]
    high_scores = [a for a in activities if a.pontuacao / a.nota_maxima > 0.85]
    
    prompt = f"""
Você é um assistente educacional. Gere um relatório ESTRUTURADO em JSON (apenas JSON, sem explicações) com o seguinte formato:

{{
  "student_id": int,
  "periodo_referencia": string,
  "desempenho_geral": "baixo|medio|alto",
  "evolucao_recente": "melhorando|estavel|piorando",
  "dificuldades_aprendizagem": string,
  "pontos_fortes_aprendizagem": string,
  "estado_emocional_geral": "baixo|medio|alto",
  "engajamento": "baixo|medio|alto",
  "risco_desempenho_baixo": "baixo|medio|alto",
  "risco_desengajamento": "baixo|medio|alto",
  "necessita_intervencao": boolean,
  "resumo_llm": string,
  "recomendacao_para_professor": string,
  "recomendacao_para_pais": string,
  "plano_acao_sugerido": string
}}

Observação do professor: {request.observacao_professor}
Observação dos pais: {request.observacao_pais}

Resumo das atividades:
- Média ponderada: {weighted_avg:.2f}
- Atividades com nota baixa: {[a.tipo for a in low_scores]}
- Atividades com nota alta: {[a.tipo for a in high_scores]}
- Observações relevantes: {[a.observacoes for a in activities if a.observacoes]}

Gere apenas o JSON válido, sem explicações extras.
"""
    return prompt
