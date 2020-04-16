text = "X-DSPAM-Confidence:    0.8475";
index_start = text.find("0")
print(float(text[index_start:]))
