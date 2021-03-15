import kenlm
import math

model = kenlm.LanguageModel("out.klm")
corpus = open("CodeSwitchingResearch/11152019_two_entropies_appended_input_R_v4.csv", 'r')
processed = open("new_corpus.csv", 'w')

# Add columns
header = corpus.readline().strip()
processed.writelines(header + ",zeb_surprisal,zeb_mutual\n")

# Process each line
i = 0
for line in corpus.readlines():
    line = line.strip()

    components = line.split(',')
    word_id = int(components[6]) - 1
    translation = components[5]

    # fourgram before the word actually ranges in length from 0 to 4
    # depending on what's available
    fourgram = ' '.join(translation.strip().split(' ')[max(0, word_id-4):word_id])
    unigram = components[8]

    # If the fourgram stretches over the beginning-of-sentence marker
    bos = (max(0, word_id-3) == 0)

    # Suprisal as -log of the conditional probability of the last word in the fivegram
    fivegram = fourgram + ' ' + unigram
    surprisal = - list(model.full_scores(fivegram, bos=bos, eos=False))[-1][0]

    # Mutual information
    p_join = pow(10, model.score(fivegram, bos=bos, eos=False))
    p_fourgram = pow(10, model.score(fourgram, bos=bos, eos=False))
    p_unigram = pow(10, model.score(unigram, bos=False, eos=False))
    mutual = math.log(p_join / (p_fourgram * p_unigram), 2)
    processed.writelines(line + ",{},{}\n".format(surprisal,mutual))
    print(i)
    i+=1

corpus.close()
processed.close()
