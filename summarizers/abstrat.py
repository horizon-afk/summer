import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def summarize(text: str):
    model = AutoModelForSeq2SeqLM.from_pretrained('t5-base')
    tokenizer = AutoTokenizer.from_pretrained('t5-base')


    tokens_input = tokenizer.encode("summarize: " + text,
                              return_tensors='pt',
                              max_length=512,
                              truncation=True)

    summary_ids = model.generate(tokens_input, min_length=80, 
                           max_length=150, length_penalty=15, 
                           num_beams=2)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
# Example usage:
input_text = """
New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, NewYork.A year later, she got married again in Westchester County, but to a different man and without
divorcing her first husband.Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it
was her "first and only" marriage.Barrientos, now 39, is facing two criminal counts of "offering a falseinstrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.Prosecutors said the marriages werepart of an immigration scam.On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking
into the New York subway through an emergency exit, said Detective Annette Markowski, a police
spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring
between 1999 and 2002. All occurred either in Westchester County, Long Island, New Jersey or the
Bronx. She is believed to still be married to four men, and at one time, she was married to eight menat once, prosecutors say. Prosecutors said the immigration scam involved some of her husbands, whofiled for permanent residence status shortly after the marriages. Any divorces happened only after
such filings were approved. It was unclear whether any of the men will be prosecuted. The case was referred to the Bronx District Attorney Office by Immigration and Customs Enforcement
and the Department of Homeland Security Investigation Division. Seven of the men are fromso-called"red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint
Terrorism Task Force.If convicted, Barrientos faces up to four years in prison. Her next court
appearance is scheduled for May 18.
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

