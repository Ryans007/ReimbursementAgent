from graph.graph import graph

if __name__ == "__main__":
    thread = {"configurable": {"thread_id": "1"}}
    for s in graph.stream({
        'user_message': "O cliente quer reembolso, mas o pedido já saiu para entrega. Ainda é permitido?",
        'label': '',
        'reimbursement_answer': '',
        'classification_agent_explaination': '',
        'confidence': 0.0,
        'messages': [],
        'final_answer': ''
    }, thread):
        print(s)