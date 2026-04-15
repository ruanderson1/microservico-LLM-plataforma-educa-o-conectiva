from schemas.class_ import ClassReportRequest

def build_class_prompt(request: ClassReportRequest) -> str:
    prompt = f"""
Você é um assistente educacional. Gere um relatório ESTRUTURADO em JSON (apenas JSON, sem explicações) com o seguinte formato:

{{
  "class_id": int,
  "periodo_referencia": string,
  "desempenho_medio_turma": "baixo|medio|alto",
  "principais_dificuldades_turma": string,
  "nivel_engajamento_turma": "baixo|medio|alto",
  "risco_desengajamento_turma": "baixo|medio|alto",
  "necessita_intervencao_coletiva": boolean,
  "resumo_llm_turma": string,
  "recomendacao_para_professor_turma": string,
  "plano_acao_turma": string
}}

Observação do professor da turma: {request.observacao_professor_turma}

Resumo dos alunos:
"""
    for s in request.students:
        prompt += f"- Aluno {s.student_id}: desempenho_geral={s.desempenho_geral}, engajamento={s.engajamento}, risco_desengajamento={s.risco_desengajamento}, dificuldades={s.dificuldades_aprendizagem}\n"
    prompt += "\nGere apenas o JSON válido, sem explicações extras."
    return prompt
