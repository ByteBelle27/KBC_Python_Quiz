questions =["What is the capital of India?",
  "Which language is used for web apps?",
  "Who is known as the father of computers?",
  "Which planet is known as the Red Planet?",
  "What is the boiling point of water?",
  "Who wrote the national anthem of India?",
  "Which gas do plants absorb?",
  "Who was the first President of India?",
  "How many continents are there in the world?",
  "What is the currency of Japan?"
]

options= [ ["a.mumbai","b.delhi","c.chennai","d.kolkata"],["a.python","b.java","c.javascript","d.c++"],["a.charles babbage","b.steve jobs","c.bill gates","d.steve wozniak"],["a.earth","b.mars","c.venus","d.jupiter"],["a.100°C","b.212°F","c.100°F","d.212°C"],["a.bankim chandra chatterjee","b.rabindranath tagore","c.swami vivekananda","d.raja ram mohan roy"],["a.oxygen","b.carbon dioxide","c.hydrogen","d.nitrogen"],["a.jawaharlal nehru","b.rajendra prasad","c.indira gandhi","d.morarji desai"],["a.5","b.6","c.7","d.8"],["a.yen","b.won","c.yuan","d.dollar"]  ]
answers =["b","c","a","b","d","b","a","b","c",]
prizes=[1000,2000,3000,5000,10000,20000,40000,80000,160000]
safemoney=0
earned=0
print("lets play kbc")
for i in range(len(questions)):
  print(f"Question{i+1}:{questions[i]}")
  for option in options[i]:
    print(option)
  userans=input("enter your answer:").lower()

  if userans==answers[i]:
    print("correct answer")
    earned+=prizes[i]
    print("you have won",earned)
    if i==3:
      safemoney=10000
    elif i==6:
      safemoney=30000
  else:
    print("wrong answer")
    print("game over")
    print("you have won",safemoney)
    break

print("congratulations you have won")
print("you have won",earned)


print("thank you for playing kaun banega pythonpati")