import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def summarize(text: str):
    model = AutoModelForSeq2SeqLM.from_pretrained('t5-base')
    tokenizer = AutoTokenizer.from_pretrained('t5-base')


    tokens_input = tokenizer.encode("summarize: " + input_text,
                              return_tensors='pt',
                              max_length=tokenizer.model_max_length,
                              truncation=True)

    summary_ids = model.generate(tokens_input, min_length=80, 
                           max_length=150, length_penalty=15, 
                           num_beams=2)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
# Example usage:
input_text = """
World War II, was a colossal struggle that spanned from 1939 to 1945, engulfed most of the globe.
The main combatants were divided into two alliances: the Allies and the Axis. The Allies, initially led
by Great Britain and France, eventually included the United States and the Soviet Union.Axis powers,
spearheaded by Nazi Germany, Fascist Italy, and Imperial Japan.The war's roots can be traced back to
unresolved grievances from World War I, particularly the harsh Treaty of Versailles imposed on
Germany. This, coupled with the rise of totalitarian dictators like Adolf Hitler in Germany, Benito
Mussolini in Italy, and militaristic expansionism in Japan, created a volatile atmosphere. The invasion
of Poland by Germany in 1939 ignited the war in Europe, with Britain and France declaring war in
response.The initial years saw Germany conquer much of Europe through blitzkrieg tactics. The tide
began to turn with the German invasion of the Soviet Union in 1941 and the Japanese attack on Pearl
Harbor in 1941, drawing the US into the war. The conflict then became a brutal fight on multiple
fronts, from the icy plains of Eastern Europe to the scorching deserts of North Africa, and the vast
Pacific Ocean.The war wasn't just fought on battlefields. Technological advancements led to the
development of new weapons like jet fighters, rockets, and the atomic bomb, dropped by the US on
Hiroshima and Nagasaki in Japan in 1945.Civilian populations also became targets, with horrific
atrocities committed by the Axis powers, particularly the Holocaust, the systematic extermination of
Jews by Nazi Germany.After immense sacrifice, the Allies emerged victorious in 1945. The war's
consequences were devastating. Millions lay dead, countless cities were destroyed, and the global
order was forever altered.
"""

# summary = summarize_text(input_text)
# print(summary[0]['summary_text'])

# import torch
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# model = AutoModelForSeq2SeqLM.from_pretrained('t5-base')
# tokenizer = AutoTokenizer.from_pretrained('t5-base')


# tokens_input = tokenizer.encode("summarize: " + input_text,
#                               return_tensors='pt',
#                               max_length=tokenizer.model_max_length,
#                               truncation=True)

# summary_ids = model.generate(tokens_input, min_length=80, 
#                            max_length=150, length_penalty=15, 
#                            num_beams=2)
# summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

if __name__ == "__main__": 
    print(summarize(input_text))

