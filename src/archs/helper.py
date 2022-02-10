from transformers import  AdamW
#from transformers import  BertForMaskedLM, AdamW
from transformers import CamembertForMaskedLM, AdamW





# ****************** helper ******************

def get_model():

    #return BertForMaskedLM.from_pretrained('bert-base-uncased')
    return CamembertForMaskedLM.from_pretrained('camembert-base')




def get_optimizer_class(name: str):

    if name == 'AdamW':

        return AdamW

    else:
        
        raise ValueError('Optimizer should be in : AdamW')