import random

def глухая_бабушка():
  """
  Имитирует диалог с глухой бабушкой, которая отвечает случайными фразами и годами.
  """
  print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
  pokas = 0
  while True:
    ввод = input("> ")
    if ввод.endswith("!"):
      if ввод.upper() == "ПОКА!":
        pokas += 1
        if pokas == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        else:
          год = random.randint(1930, 1950)
          print(f"НЕТ, НИ РАЗУ С {год} ГОДА!")
      else:
        pokas = 0
        год = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {год} ГОДА!")
    else:
      pokas = 0
      print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")


if __name__ == "__main__":
  глухая_бабушка()