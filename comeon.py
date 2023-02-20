from parrot import Parrot

import azuretranslation

parrot = Parrot()

phrases = [('Pain')
]

for phrase in phrases:
  print("-"*100)
  print("Input_phrase: ", phrase)
  print("-"*100)
  paraphrases = parrot.augment(input_phrase=phrase, use_gpu=False)
  if paraphrases:
    for paraphrase in paraphrases:
        paraphrase = azuretranslation.engtochi(str(paraphrase))
        print(paraphrase)