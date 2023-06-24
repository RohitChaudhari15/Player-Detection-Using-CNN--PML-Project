import numpy as np
def GuessPlayer(yhat):
    if (np.argmax(yhat)) == 0:
        return "M. S. DHONI"
    elif(np.argmax(yhat)) == 1:
        return "SACHIN TENDULKAR"     
    elif(np.argmax(yhat)) == 2:
        return "SURYAKUMAR YADAV"  
    elif(np.argmax(yhat)) == 3:
        return "SMRITI MANDHANA"
    elif(np.argmax(yhat)) == 4:
        return "VIRAT KOHLI"
    elif(np.argmax(yhat)) == 5:
        return "YUZVENDRA CHAHAL"