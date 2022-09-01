from vigerene import vigerene

print(vigerene('the quick brown fox jumps over the fence', 'helloworld1'))
print(vigerene(vigerene('the quick brown fox jumps over the fence', 'helloworld1'), 'helloworld1', True))
