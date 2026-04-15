import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    resp = requests.get(f"{BASE_URL}/health")
    print("HEALTH RESPONSE:", resp.status_code, resp.text)

def test_student_report():
    payload = {
        "student_id": 1,
        "periodo_referencia": "2024-1",
        "observacao_professor": "Aluno participativo, mas com dificuldades em matemática.",
        "observacao_pais": "Em casa, demonstra interesse pelas tarefas.",
        "atividades": [
            {"tipo": "Prova", "nota_maxima": 10, "pontuacao": 6, "peso": 2, "observacoes": "Errou questões de lógica."},
            {"tipo": "Trabalho", "nota_maxima": 10, "pontuacao": 9, "peso": 1, "observacoes": "Bom desempenho."}
        ]
    }
    resp = requests.post(f"{BASE_URL}/reports/student", json=payload)
    print("STUDENT REPORT RESPONSE:", resp.status_code, resp.text)

def test_class_report():
    payload = {
        "class_id": 101,
        "periodo_referencia": "2024-1",
        "observacao_professor_turma": "Turma engajada, mas alguns alunos com dificuldades em leitura.",
        "students": [
            {"student_id": 1, "desempenho_geral": "medio", "engajamento": "alto", "risco_desengajamento": "baixo", "dificuldades_aprendizagem": "matemática"},
            {"student_id": 2, "desempenho_geral": "baixo", "engajamento": "medio", "risco_desengajamento": "medio", "dificuldades_aprendizagem": "leitura"}
        ]
    }
    resp = requests.post(f"{BASE_URL}/reports/class", json=payload)
    print("CLASS REPORT RESPONSE:", resp.status_code, resp.text)

if __name__ == "__main__":
    test_health()
    test_student_report()
    test_class_report()
