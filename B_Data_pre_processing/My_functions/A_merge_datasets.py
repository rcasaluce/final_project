import pandas as pd
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def merge_select_columns(*args, labels = 'Yes', abstracts = 'Yes'):
    
    """
    The function returns a merged data set
    
    Parameters
    ----------
    *args : two or more data sets
    labels : bool
        A flag used to either or not add the label column (default is Yes)
    abstracts : bool
        A flag used to specified if the abstracts are needed or claism (default is Yes)
    
    Returns
    -------
    a merged dataset with only three or four columns
       
    """
    db = pd.DataFrame()
    
    dt_frames = []
    

    for data in args:
        
        if abstracts == 'Yes':
            df = data[data['type']=='Abstract']
        else:
            df = data[data['type']!='Abstract']
        
        if labels == 'Yes':
            df = pd.DataFrame({ 'publn_nr' : df['publn_nr'] ,'type': df['type'], 'label': df['class'], 'text': df['text']})
        else:
            df = pd.DataFrame({ 'publn_nr' : df['publn_nr'] ,'type': df['type'], 'text': df['text']})
        
        dt_frames.append(df)
        
        
    db = pd.concat(dt_frames) 
    
    
    return db





def pre_process_db(dataset):
    
    """
    The function splits the text in tokens,
    eliminates puntaction, numbers and 
    reduces the verbs to their lemma.
    
    Parameters
    ----------
    dataset : dataset merged
    
    Returns
    -------
    The input dataset with a extra column which is the text cleaned 
    
    """
    
    #parse claims
    stop_words = set(stopwords.words('english'))
    word_lemmatizer = WordNetLemmatizer()
    tokenizer = RegexpTokenizer(r'\w+(?:[-\\]\w+)?')#keeps words with hyphen and words back slash (problem it doubles the slash)

    list_num = str(list((range(10))))

    da = []
    for i in range(len(dataset)):
        text = dataset['text'].iloc[i]
        text = tokenizer.tokenize(str(text))
        text =  [x.lower() for x in text]
        for k in range(len(text)):
            if len(text[k]) !=0:
                if text[k][0] in list_num or text[k] in stop_words:
                    #it adds a with space insted of a number or a stop word
                    text[k] = ''
                else:
                    text[k] = word_lemmatizer.lemmatize(text[k], pos="v")
        text = ' '.join(filter(None,text))#filter and None help to elimate white spaces in the list of strings

        da.append(text)   
        
    dataset['text_clean'] = da
        
    return dataset 


if __name__ == "__main__":
    main()
