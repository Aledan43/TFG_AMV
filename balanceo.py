benign_count = len(data[data.etiqueta == 1])
malicious_data = data[data.etiqueta == 0 ]

malicious_sample = malicious_data.sample(n=benign_count, random_state=42)

balanced_data = pd.concat([data[data.etiqueta == 1 ], malicious_sample])
balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)
print(balanced_data.etiqueta.value_counts())