Questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["A. Chittagong", "B. Dhaka", "C. Rangpur", "D. Sylhet"],
        "answer": "B"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Kolkata", "C. Delhi", "D. Chennai"],
        "answer": "C"
    },
    {
        "question": "What is the capital of the United States?",
        "options": ["A. New York", "B. Washington, D.C.", "C. Los Angeles", "D. Chicago"],
        "answer": "B"
    },
    {
        "question": "What is the capital of the United Kingdom?",
        "options": ["A. Liverpool", "B. Manchester", "C. London", "D. Birmingham"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montreal"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Tokyo", "B. Kyoto", "C. Osaka", "D. Hiroshima"],
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Lyon", "C. Marseille", "D. Bordeaux"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["A. Frankfurt", "B. Berlin", "C. Hamburg", "D. Munich"],
        "answer": "B"
    },
    {
        "question": "What is the capital of China?",
        "options": ["A. Shanghai", "B. Guangzhou", "C. Beijing", "D. Shenzhen"],
        "answer": "C"
    }
]


result=0
print("welcome to Quiz game")
for q in Questions:
    print(q['question'])
    for op in q['options']:
        print(op)
    your_answer= input("your answer{A,B,C,D} : ").strip().upper()
    
    if your_answer == q['answer']:
        print("Answer is correct!")
        result=result+1
    else:
        print(f"wrong answer.correct answer was :{q['answer']}")

print(f"final score : {result} out of {len(Questions)}")