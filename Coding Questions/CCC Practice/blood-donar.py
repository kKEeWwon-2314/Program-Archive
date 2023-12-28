# https://dmoj.ca/problem/ccc11s4
# CCC 2011 S4 - Blood Distribution

from unittest import result


blood = list(map(int, input().split()))
patient = list(map(int, input().split()))

extraON = 0
extraOP = 0
extraAN = 0
extraAP = 0
extraBN = 0
extraBP = 0
extraABN = 0
extraABP = 0
max_patient = 0

for i in range(8):
    if (blood[i] >= patient[i]):
        if (i == 0):
            max_patient += patient[i]
            extraON = blood[i] - patient[i]
        elif (i == 1):
            max_patient += patient[i]
            extraOP = blood[i] - patient[i]
        elif (i == 2):
            max_patient += patient[i]
            extraAN = blood[i] - patient[i]
        elif (i == 3):
            max_patient += patient[i]
            extraAP = blood[i] - patient[i]
        elif (i == 4):
            max_patient += patient[i]
            extraBN = blood[i] - patient[i]
        elif (i == 5):
            max_patient += patient[i]
            extraBP = blood[i] - patient[i]
        elif (i == 6):
            max_patient += patient[i]
            extraABN = blood[i] - patient[i]
        elif (i == 7):
            max_patient += patient[i]
            extraABP = blood[i] - patient[i]
    else:
        if (i == 0): # O-: O-
            max_patient = blood[i]
        elif (i == 1): # O+: O+,O-
            blood[i] += extraON
            if (blood[i] > patient[i]):
                extraON = blood[i] - patient[i]
                max_patient += patient[i]
            else:
                extraON = 0
                max_patient += blood[i]
        elif (i == 2): # A-: A-,O-
            blood[i] += extraON
            if (blood[i] > patient[i]):
                max_patient += patient[i]
                if (blood[i] - patient[i]) >= extraON:
                    extraAN = blood[i] - patient[i] + extraON
                else:
                    extraON = blood[i] - patient[i]
                    extraAN = 0
        elif (i == 3): # A+: A+,O+,A-,O-
            blood[i] += (extraAP + extraOP + extraAN + extraON)
            if blood[i] >= patient[i]:
                max_patient += patient[i]
                if ((blood[i] - patient[i]) >= (extraAN + extraON + extraOP)):
                    extraAP = blood[i] - patient[i] - extraAP - extraON - extraOP
                elif ((blood[i] - patient[i]) >= (extraON + extraOP)):
                    extraAN = blood[i] - patient[i] - extraON - extraOP
                    extraAP = 0
                elif ((blood[i] - patient[i]) >= extraON):
                    extraOP = blood[i] - patient[i] - extraON
                    extraAN = 0
                    extraAP = 0
                else:
                    extraON = blood[i] - patient[i] 
                    extraAN = 0
                    extraAP = 0
                    extraOP = 0
            else:
                max_patient += blood[i]
                extraAN = 0
                extraAP = 0
                extraON = 0
                extraOP = 0
        elif (i == 4): # B-: B-,O-
            blood[i] += extraON
            if blood[i] >= patient[i]:
                extraON = blood[i] - patient[i]
                max_patient = max_patient + patient[i]
            else:
                extraON = 0
                max_patient = max_patient + blood[i]
        elif (i == 5): # B+: B+,O+,B-,O-
            patient[i] += (extraBP + extraOP + extraBN + extraON)
            if (blood[i] > patient[i]):
                max_patient += patient[i]
                if ((blood[i] - patient[i]) >= (extraBN + extraON + extraOP)):
                    extraBP = blood[i] - patient[i] - extraBP - extraON - extraOP 
                elif ((blood[i] - patient[i] ) >= (extraON + extraOP)):
                    extraBN = blood[i] - patient[i] - extraON - extraOP
                    extraBP = 0
                elif ((blood[i] - patient[i]) >= (extraON)):
                    extraOP = blood[i] - patient[i] - extraON
                    extraBN = 0
                    extraBP = 0
                else: 
                    extraON = blood[i] - patient[i] 
                    extraBN = 0
                    extraBP = 0
                    extraOP = 0
            else: 
                max_patient += blood[i]
                extraBN = 0
                extraBP = 0
                extraON = 0
                extraOP = 0
        elif (i == 6): # AB-: AB-,A-,B-,O-
            patient[i] += (extraABN + extraAN + extraBN + extraON)
            if (blood[i] > patient[i]):
                max_patient += patient[i]
                if ((blood[i] - patient[i]) >= (extraAN + extraBN + extraON)):
                    extraABN = blood[i] - patient[i] - extraAN - extraBN - extraON
                elif ((blood[i] - patient[i] ) >= (extraAN + extraON)):
                    extrbN = blood[i] - patient[i] - extraON - extraAN
                    extraABN = 0
                elif ((blood[i] - patient[i]) >= extraON):
                    extraAN = blood[i] - patient[i] - extraON
                    extraBN = 0
                    extraABN = 0
                else:
                    extraON = blood[i] - patient[i]
                    extraAN = 0
                    extraBN = 0
                    extraABN = 0
            else:
                max_patient += blood[i]
                extraABN = 0
                extraAN = 0
                extraBN = 0
                extraON = 0
        elif (i == 7): # AB+: LITERALY EVERYTHING
            patient[i] += (extraON + extraOP + extraAN + extraAP + extraBN + extraBP + extraABN + extraABP)
            if (blood[i] >= patient[i]):
                max_patient += patient[i]
            else:
                max_patient += blood[i]

print(max_patient)